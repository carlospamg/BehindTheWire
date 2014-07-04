from __future__ import unicode_literals
import os
import Tkinter
import tkFileDialog
from ServerCompilerSettings import ServerCompilerSettings
from SketchCreator import SketchCreator


def execute_command_line():
    """ Launches a command line with the input string """
    # Concatenates the command string
    command_line_command = ServerCompilerSettings().compiler_dir + ' '
    if not ServerCompilerSettings().launch_IDE_only:
        command_line_command += '--upload '
        command_line_command += '--board ' + \
            ServerCompilerSettings().sketch_dir + ' '
    command_line_command += '"' + create_sketch_from_string() + '"'
    print('Command line command:\n\t' + command_line_command)
    os.system(command_line_command)


def create_sketch_from_string():
    return SketchCreator().create_sketch()


def browse_file():
    root = Tkinter.Tk()
    root.withdraw()
    types = [('Executable', '.exe'), ('All Files', '*')]
    file_path = tkFileDialog.askopenfilename(filetypes=types)
    root.destroy()
    return file_path


def browse_dir():
    root = Tkinter.Tk()
    root.withdraw()
    file_path = tkFileDialog.askdirectory(
        parent=root, initialdir="/", title='Please select a directory')
    root.destroy()
    return file_path


def set_compiler_path():
    ServerCompilerSettings().compiler_dir = browse_file()


def get_compiler_path():
    return ServerCompilerSettings().compiler_dir


def set_sketch_path():
    ServerCompilerSettings().compiler_dir = browse_dir()


def get_sketch_path():
    return ServerCompilerSettings().compiler_dir


def main():
    print("This is the BlocklyRequestHandler main")


if __name__ == "__main__":
    main()
