from __future__ import unicode_literals, absolute_import
import os
import BaseHTTPServer
import SimpleHTTPServer
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
        #content_type = self.headers.getheader('content-type')
        #TODO: Look for a non-decrecated content-type to replace form
        #if not contentType.startswith('application/x-www-form-urlencoded'):
        #    self.send_response(404, "oh, shiny!")
        #    self.send_header('Content-type', 'text/plain')
        #    self.end_headers()
        #    self.wfile.write('Error: only accepting form data')
        #    return
        #post_variables = self.parse_POST()
        #action = post_variables.get("action")[0]
        
        content_length = int(self.headers.getheader('content-length'))
        data_string = self.rfile.read(content_length)
        try:
            message_back = '//Python test\n\r' + data_string
        except Exception as e:
            print(e)
            print('There was an error manipulating the POST data!!!')
            message_back = 'error'

        sketch_path = BlocklyRequestHandler.create_sketch_from_string(message_back)
        BlocklyRequestHandler.load_sketch(sketch_path)
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
