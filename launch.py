import threading
import webbrowser
import os
import BlocklyServerCompiler

BLOCKLY_INDEX = 'blockly/apps/blocklyduino/index.html'
PORT = 8000


def open_browser():
    """Start a browser after waiting for half a second."""
    def _open_browser():
        webbrowser.open('http://127.0.0.1:%s/%s' % (PORT, BLOCKLY_INDEX))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()


if __name__ == "__main__":
    open_browser()
    test_instance = BlocklyServerCompiler.SketchCreator()
    test_instance.create_sketch()
    BlocklyServerCompiler.start_server(os.getcwd())
