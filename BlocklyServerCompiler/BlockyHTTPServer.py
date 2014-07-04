import os
import BaseHTTPServer
import SimpleHTTPServer
import json
import BlocklyRequestHandler

PORT = 8000

class BlockyHTTPServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """Simple Python server to pass over the AJAX requests
       This class will only deal with receiving and decoding messages,
       and a different handler will deal with the requests """
    
    def do_POST(self):
        """Handle a post request by returning the text with an added string"""
        
        length = int(self.headers.getheader('content-length'))
        data_string = self.rfile.read(length)
        try:
            result = '//Python test\n\r' + data_string
        except:
            result = 'error'
        
        BlocklyRequestHandler.execute_command_line()
        
        self.wfile.write(result)


def start_server(DocumentRoot):
    """Start the server with the document root indicated by argument"""
    print('Setting HTTP Server Document Root to: \n\t' + DocumentRoot + "\n")
    os.chdir(DocumentRoot)
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, BlockyHTTPServer)
    print('Launching the HTTP service...')
    server.serve_forever()
    print('Something went wrong!!')


if __name__ == "__main__":
    start_server(os.getcwd())
