import threading
import webbrowser
import os
from BlocklyServerCompiler import *

FILE = 'blockly/apps/blocklyduino/index.html'
PORT = 8000


def open_browser():
    """Start a browser after waiting for half a second."""
    def _open_browser():
        webbrowser.open('http://127.0.0.1:%s/%s' % (PORT, FILE))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()


if __name__ == "__main__":
    open_browser()
    start_server(os.getcwd())
