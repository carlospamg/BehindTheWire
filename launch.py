#!python2
###############################################################################
# The comment above works if the Python Launcher for Windows path included
# in Python>3.3  does not conflict with the py.exe file added to "C:\Windows"
# In the future will try to either port the entire app to version 3 or
# make it compatible with both 2.x and 3.x
###############################################################################
import os
import platform
import threading
import webbrowser
import BlocklyServerCompiler

BLOCKLY_INDEX = 'blockly/apps/blocklyduino/index.html'
PORT = 8000


def open_browser():
    """Start a browser after waiting for half a second."""
    def _open_browser():
        webbrowser.open('http://127.0.0.1:%s/%s' % (PORT, BLOCKLY_INDEX))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()


def main(): 
    print("Running Python version " + platform.python_version() + "\n")
    BlocklyServerCompiler.BlocklyRequestHandler().browse_compiler_executable()
    open_browser()
    test_instance = BlocklyServerCompiler.SketchCreator()
    test_instance.create_sketch()
    print(list(BlocklyServerCompiler.serial_ports()))
    BlocklyServerCompiler.start_server(os.getcwd())
    


if __name__ == "__main__":
    main()
