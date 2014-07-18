from __future__ import unicode_literals, absolute_import
import os
import Tkinter
import tkFileDialog
from BlocklyServerCompiler.Py23Compatibility import Py23Compatibility
from BlocklyServerCompiler.ServerCompilerSettings import ServerCompilerSettings
from BlocklyServerCompiler.SketchCreator import SketchCreator


def load_sketch(sketch_path=None):
    """
    Launches a command line that invokes the Arduino IDE to open and/or
    load an sketch, which address is indicated in the input parameter
    """
    # Input sanitation
    if not isinstance(sketch_path, Py23Compatibility.string_type_compare) \
            or not sketch_path:
        sketch_path = create_sketch_default()

    # Concatenates the command string
    command_line_command = ServerCompilerSettings().compiler_dir + ' '
    if not ServerCompilerSettings().launch_IDE_only:
        command_line_command += '--upload '
        command_line_command += '--port ' + \
            ServerCompilerSettings().com_port + ' '
        command_line_command += '--board ' + \
            ServerCompilerSettings().get_arduino_board_flag() + ' '
    command_line_command += '"' + sketch_path + '"'
    print('Command line command:\n\t' + command_line_command)
    os.system(command_line_command)


def create_sketch_default():
    return SketchCreator().create_sketch()


def create_sketch_from_string(sketch_code):
    return SketchCreator().create_sketch(sketch_code)


def browse_file():
    """
    Opens a file browser and selects executable files
    :return: Full path to selected file
    """
    #TODO: Manually set to filder .exe files, need to make it compatible
    #      with other OSes
    root = Tkinter.Tk()
    root.withdraw()
    types = [('Executable', '.exe'), ('All Files', '*')]
    file_path = tkFileDialog.askopenfilename(filetypes=types)
    root.destroy()
    return file_path


def browse_dir():
    """
    Opens a directory browser to select a folder
    :return: Full path to the selected folder
    """
    root = Tkinter.Tk()
    root.withdraw()
    file_path = tkFileDialog.askdirectory(
        parent=root, initialdir="/", title='Please select a directory')
    root.destroy()
    return file_path


def set_compiler_path():
    """
    Open the file browser to select a file. Saves this filepath into
    ServerCompilerSettings and if the filepath is different to that stored
    already it triggers the new data to be saved into the settings file.
    """
    current_path = get_compiler_path()
    new_path = browse_file()

    if new_path != '':
        ServerCompilerSettings().compiler_dir = new_path
        if current_path != get_compiler_path():
            ServerCompilerSettings().save_settings()
    else:
        new_path = None

    return new_path


def get_compiler_path():
    return ServerCompilerSettings().compiler_dir


def set_sketch_path():
    """
    Open the directory browser to select a file. Saves this directory into
    ServerCompilerSettings and if the directory is different to that stored
    already it triggers the new data to be saved into the settings file.
    """
    old_directory = get_sketch_path()
    new_directory = browse_dir()
    if new_directory != '':
        ServerCompilerSettings().sketch_dir = browse_dir()
        if old_directory != get_sketch_path():
            ServerCompilerSettings().save_settings()


def get_sketch_path():
    return ServerCompilerSettings().sketch_dir


def main():
    print("This is the BlocklyRequestHandler main.")


if __name__ == "__main__":
    main()
