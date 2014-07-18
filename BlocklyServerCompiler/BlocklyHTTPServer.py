from __future__ import unicode_literals, absolute_import
import os
import BaseHTTPServer
import SimpleHTTPServer
import cgi
import urlparse
from BlocklyServerCompiler import BlocklyRequestHandler

PORT = 8000


class BlocklyHTTPServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """
    Simple Python server to pass over the AJAX requests
    This class will only deal with receiving and decoding messages,
    and a different handler will deal with the requests
    """
    
    def do_POST(self):
        """
        Serves the POST request, using form-like data
        """
        message_back = ''
        parameters = None
        content_type, parameters_dict = cgi.parse_header(
            self.headers.getheader('content-type'))
        content_length = int(self.headers.getheader('content-length'))

        if content_type == 'multipart/form-data':
            parameters = cgi.parse_multipart(self.rfile, parameters_dict)
            #TODO: deal with multipart form data, might not be necessary though
        elif content_type == 'application/x-www-form-urlencoded':
            parameters = urlparse.parse_qs(self.rfile.read(content_length), keep_blank_values=False)
            for key in parameters:
                print(str(key) + ": " + str(parameters[key]))
            #parameters = cgi.FieldStorage(
            #    fp=self.rfile,
            #    headers=self.headers,
            #    environ={'REQUEST_METHOD':'POST',
            #             'CONTENT_TYPE':self.headers['Content-Type'], })
            #for item in parameters.list:
            #    print(item)
        elif content_type == 'text/plain':
            data_string = self.rfile.read(content_length)
            try:
                message_back = '//Python test\n\r' + data_string
            except Exception as e:
                print(e)
                print('\nThere was an error manipulating the plain text data!!!')
        else:
            print('\nError, content type not recognised: ' + str(content_type))
            self.send_response(404, "Upps, not found!")
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Error: invalid content type')
            return

        if message_back != '':
            #sketch_path = BlocklyRequestHandler.create_sketch_from_string(message_back)
            #BlocklyRequestHandler.load_sketch(sketch_path)
            pass

        if parameters:
            for key in parameters:
                if str(key) == 'compiler':
                    if str(parameters[key]) == "['get']":
                        message_back = BlocklyRequestHandler.get_compiler_path()
                    elif str(parameters[key]) == "['set']":
                        message_back = BlocklyRequestHandler.set_compiler_path()
                else:
                    print('Ups')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message_back)


def start_server(document_root):
    """ Start the server with the document root indicated by argument """
    print('\nSetting HTTP Server Document Root to: \n\t' + document_root + "\n")
    os.chdir(document_root)
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, BlocklyHTTPServer)
    print('Launching the HTTP service...')
    server.serve_forever()
    print('Something went wrong!!')


if __name__ == "__main__":
    start_server(os.getcwd())
