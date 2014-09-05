#!/usr/bin/env python2
# ##############################################################################
# The comment above works if the Python Launcher for Windows path included
# in Python>3.3 does not conflict with the py.exe file added to "C:\Windows"
# In the future will attempt to make the entire application compatible with
# both 2.5+ and 3.x
###############################################################################
from __future__ import unicode_literals, absolute_import
import os
import platform
import threading
import webbrowser
try:
    # 2.x name
    import BaseHTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler
except ImportError:
    # 3.x name
    import http.server as BaseHTTPServer
    from http.server import SimpleHTTPRequestHandler as SimpleHTTPRequestHandler

    
ADDRESS = 'localhost'
PORT = 8000


def start_server(document_root):
    """ Start the server with the document root indicated by argument """
    print('\nSetting HTTP Server Document Root to: \n\t' + document_root + "\n")
    os.chdir(document_root)
    server_class  = BaseHTTPServer.HTTPServer
    server_address = (ADDRESS, PORT)
    handler_class = SimpleHTTPRequestHandler
    server = server_class(server_address, handler_class)
    print('Launching the HTTP service...')
    server.serve_forever()
    print('The Server closed unexpectedly!!')


def open_browser():
    """ Start a browser after waiting for half a second. """

    def _open_browser():
        webbrowser.open('http://%s:%s/%s' %
                        (ADDRESS, PORT, 'blockly/apps/blocklyduino/index.html'))

    thread = threading.Timer(0.5, _open_browser)
    thread.start()


def main():
    print('Running Python version ' + platform.python_version())
    open_browser()
    start_server(os.getcwd())


if __name__ == "__main__":
    main()
