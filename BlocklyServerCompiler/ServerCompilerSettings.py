from __future__ import unicode_literals
import os
import ConfigParser


class ServerCompilerSettings(object):
    """
    Retrieves and saves the settings for the server side compilation.
    No compiler is part of the Python code, instead settings that 
    point to the local Arduino IDE and sketch are stored here.
    """

    # Designed to be immutable variables
    __singleton_instance__ = None
    __settings_filename__ = "ServerCompilerSettings.ini"
    __settings_path__ = "ServerCompilerSettings.ini"

    # Settings with getters and setters
    __launch_IDE_only__ = False
    __compiler_dir__ = 'C:\\IDEs\\arduino-1.5.6-r2\\arduino.exe'
    __sketch_dir__ = 'G:\\GE\\CSF\\git\\BlocklyDuino'
    __sketch_name__ = 'BlocklyDuinoSketch'
    __arduino_types__ = {'Uno': 'arduino:avr:uno',
                         'Leonardo': 'arduino:avr:leonardo',
                         'Mega': 'arduino:avr:mega',
                         'Duemilanove_328p': 'arduino:avr:diecimila',
                         'Duemilanove_168p': 'arduino:avr:diecimila:cpu=atmega168'}
    __arduino_board__ = __arduino_types__['Uno']

    #
    # Singleton creator 
    #
    def __new__(cls, *args, **kwargs):
        """ Creating or returning the singleton instance """
        if not cls.__singleton_instance__:
            # Create the singleton instance
            cls.__singleton_instance__ =\
                super(ServerCompilerSettings, cls).__new__(cls, *args, **kwargs)
            # Initialise the instance
            read_successfully = cls.__singleton_instance__.read_settings()
            if not read_successfully:
                cls.__sketch_dir__ = os.getcwd()
        return cls.__singleton_instance__

    #
    # Getters and Setters
    #
    def get_compiler_dir(cls):
        return cls.__compiler_dir__

    def set_compiler_dir(cls, new_compiler_dir):
        """ The compiler dir must be full path to an .exe file """
        # FIXME: this is a windows only check (.exe), needs to be
        #        updated to be compatible with linux and MacOS
        if os.path.exists(new_compiler_dir) and\
                new_compiler_dir.endswith('.exe'):
            cls.__compiler_dir__ = new_compiler_dir
        else:
            print('The provided compiler path is not valid !!!')
            print('\t' + new_compiler_dir)

    compiler_dir = property(get_compiler_dir, set_compiler_dir)

    def get_sketch_name(cls):
        return cls.__sketch_name__

    def set_sketch_name(cls, new_sketch_name):
        cls.__sketch_name__ = new_sketch_name

    sketch_name = property(get_sketch_name, set_sketch_name)

    def get_sketch_dir(cls):
        return cls.__sketch_dir__

    def set_sketch_dir(cls, new_sketch_dir):
        """ The sketch directory must be a folder """
        if os.path.isdir(new_sketch_dir):
            cls.__sketch_dir__ = new_sketch_dir
        else:
            print('The provided sketch directory is not valid !!!')
            print('\t' + new_sketch_dir)

    sketch_dir = property(get_sketch_dir, set_sketch_dir)

    def get_launch_ide_only(cls):
        return cls.__launch_IDE_only__

    def set_launch_ide_only(cls, new_launch_IDE_only):
        cls.__launch_IDE_only__ = new_launch_IDE_only

    launch_IDE_only = property(get_launch_ide_only, set_launch_ide_only)

    #
    # Settings file
    #
    def save_settings(cls):
        settings_parser = ConfigParser.ConfigParser()
        settings_parser.add_section('Arduino_IDE')
        settings_parser.set(
            'Arduino_IDE',
            'Arduino_Exec_Path',
            cls.__compiler_dir__)
        settings_parser.set(
            'Arduino_IDE',
            'Arduino_Board',
             cls.__compiler_dir__)
        settings_parser.set(
            'Arduino_IDE',
            'Arduino_COM_Port',
            cls.__compiler_dir__)
        settings_parser.add_section('Arduino_Sketch')
        settings_parser.set(
            'Arduino_Sketch',
            'Sketch_Name',
             cls.__sketch_name__)
        settings_parser.set(
            'Arduino_Sketch',
            'Sketch_Directory',
            cls.__sketch_dir__)

        # Set the path and create/overwrite the file
        cls.__settings_path__ = os.path.join(
            os.getcwd(), cls.__settings_filename__)
        settings_file = open(cls.__settings_path__, 'w')
        settings_parser.write(settings_file)
        settings_file.close()

    def read_settings(cls):
        """ TODO: this operation """
        return False

    def delete_settings(cls):
        if os.path.exists(cls.__settings_path__):
            os.remove(cls.__settings_path__)


def main():
    """ This should never be executed """
    print("This is the ServerCompilerSettings main")


if __name__ == '__main__':
    main()
