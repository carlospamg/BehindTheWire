import os
import Tkinter, tkFileDialog
from ServerCompilerSettings import ServerCompilerSettings


def execute_command_line():
    """ Launches a command line with the input string """
    # Concadenate the command string
    command_line_command = ServerCompilerSettings().compiler_dir + ' '
    if ServerCompilerSettings().launch_IDE_only:
        command_line_command += '--upload '
        command_line_command += '--board arduino:' + \
            ServerCompilerSettings().arduino_board + ' '
    command_line_command += '"' + ServerCompilerSettings().sketch_dir + '"'
    print('Command line command:\n\t' + command_line_command)
    os.system(command_line_command)


def browse_file():
    root = Tkinter.Tk()
    root.withdraw()
    file_path = tkFileDialog.askopenfilename()
    print(file_path)
    return file_path


def set_compiler_path():
    ServerCompilerSettings().compiler_dir = browse_file()


def get_compiler_path():
    return ServerCompilerSettings().compiler_dir


def set_sketch_path():
    ServerCompilerSettings().compiler_dir = browse_file()


def get_sketch_path():
    return ServerCompilerSettings().compiler_dir


def main():
    print("This is the BlocklyRequestHandler main")


if __name__ == "__main__":
    main()
