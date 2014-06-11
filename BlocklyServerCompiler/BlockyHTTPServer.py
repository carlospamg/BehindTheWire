import BaseHTTPServer
import SimpleHTTPServer
import os

PORT = 8000

class BlockyHTTPServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """Simple Python server to pass over the AJAX requests"""
        
    def do_POST(self):
        """Handle a post request by returning the text with an added string"""
        length = int(self.headers.getheader('content-length'))
        data_string = self.rfile.read(length)
        try:
            result = '//Python test\n\r' + data_string
        except:
            result = 'error'
        self.launch_command_line()
        self.wfile.write(result)

    def launch_command_line(self):
        command_line_command = '"C:\\IDE\\arduino-1.5.6-r2\\arduino.exe"'
        print('Command line command:\n\t' + command_line_command)
        os.system(command_line_command)

        
class BlocklyRequestHandler():
    """Request Handler from the BlockyDuino app"""


def start_server(DocumentRoot):
    """Start the server with the document root indicated by argument"""
    print('Setting HTTP Server Document Root to: ' + DocumentRoot)
    os.chdir(DocumentRoot)
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, BlockyHTTPServer)
    print('Launching the HTTP service...')
    server.serve_forever()
    print('Something went wrong!!')


if __name__ == "__main__":
    start_server(os.getcwd())
