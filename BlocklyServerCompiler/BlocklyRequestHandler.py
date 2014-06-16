import os
import Tkinter, tkFileDialog
from ServerCompilerSettings import ServerCompilerSettings


def launch_command_line():
    # Concadenate the command string
    command_line_command = ServerCompilerSettings().compiler_dir + ' ' + \
        '--upload ' + \
        '--board arduino:avr:uno ' + \
        '"' + ServerCompilerSettings().sketch_dir + '"'
    print('Command line command:\n\t' + command_line_command)
    os.system(command_line_command)


def browse_compiler_executable():
    root = Tkinter.Tk()
    root.withdraw()
    file_path = tkFileDialog.askopenfilename()
    print(file_path)
    return file_path


def main():
    print("This is the BlocklyRequestHandler main")


if __name__ == "__main__":
    main()
