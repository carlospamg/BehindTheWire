#!/usr/bin/env python2
###############################################################################
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
import BlocklyServerCompiler.ServerCompilerSettings
import BlocklyServerCompiler.BlockyHTTPServer
import BlocklyServerCompiler

BLOCKLY_INDEX = 'blockly/apps/blocklyduino/index.html'
PORT = 8000


def open_browser():
    """ Start a browser after waiting for half a second. """
    def _open_browser():
        webbrowser.open('http://127.0.0.1:%s/%s' % (PORT, BLOCKLY_INDEX))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()


def main(): 
    print('Running Python version ' + platform.python_version() + "\n")
    #print("Selected file: ")
    #BlocklyServerCompiler.BlocklyRequestHandler.browse_compiler_executable()
    #BlocklyServerCompiler.BlocklyRequestHandler.launch_command_line()
    #print("\nList of available ports:")
    #BlocklyServerCompiler.PySerialListPorts.list_ports.main()
    open_browser()
    print("")
    BlocklyServerCompiler.BlockyHTTPServer.start_server(os.getcwd())
    

if __name__ == "__main__":
    main()
