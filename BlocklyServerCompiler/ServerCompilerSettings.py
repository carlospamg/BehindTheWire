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
    __settings_filename__ = 'ServerCompilerSettings.ini'
    __settings_path__ = None

    # This is a static dictonary to have board types
    __arduino_types__ = {'Uno': 'arduino:avr:uno',
                         'Leonardo': 'arduino:avr:leonardo',
                         'Mega': 'arduino:avr:mega',
                         'Duemilanove_328p': 'arduino:avr:diecimila',
                         'Duemilanove_168p': 'arduino:avr:diecimila:cpu=atmega168'}

    # Settings with accessors
    __launch_IDE_only__ = None
    __compiler_dir__ = None
    __sketch_dir__ = None
    __sketch_name__ = None
    __arduino_board_key__ = None
    __arduino_board_value__ = None
    __com_port__ = None

    #
    # Singleton creator and destructor
    #
    def __new__(cls, *args, **kwargs):
        """ Creating or returning the singleton instance """
        if not cls.__singleton_instance__:
            # Create the singleton instance
            cls.__singleton_instance__ =\
                super(ServerCompilerSettings, cls).__new__(cls, *args, **kwargs)
            # Initialise the instance, defaults if file not found
            cls.__singleton_instance__.read_settings()
        return cls.__singleton_instance__

    def _drop(cls):
        """ Drop the instance """
        cls.__singleton_instance__ = None
        del cls.__singleton_instance__

    #
    # Getters, Setters and defaults
    #
    # Compiler Directory
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

    def set_compiler_dir_default(cls):
        cls.__compiler_dir__ = 'C:\\IDEs\\arduino-1.5.6-r2\\arduino.exe'

    # Arduino Board and board lists
    def get_arduino_board(cls):
        return cls.__arduino_board_key__

    def set_arduino_board(cls, new_board):
        if new_board in cls.__arduino_types__:
            cls.__arduino_board_value__ = cls.__arduino_types__[new_board]
            cls.__arduino_board_key__ = new_board
        else:
            cls.verify_settings()
            print('Arduino Board in settings file does not exists')

    arduino_board = property(get_arduino_board, set_arduino_board)

    def set_arduino_board_default(cls):
        cls.__arduino_board_key__ = 'Uno'
        cls.__arduino_board_value__ = \
            cls.__arduino_types__[cls.__arduino_board_key__]

    def get_arduino_board_flag(cls):
        return cls.__arduino_board_value__

    def get_arduino_board_types(cls):
        board_list = []
        for key in cls.__arduino_types__:
            board_list.append(key)
        return board_list

    # Sketch name
    def get_sketch_name(cls):
        return cls.__sketch_name__

    def set_sketch_name(cls, new_sketch_name):
        cls.__sketch_name__ = new_sketch_name

    sketch_name = property(get_sketch_name, set_sketch_name)

    def set_sketch_name_default(cls):
         cls.__sketch_name__ = 'BlocklyDuinoSketch'

    # Sketch Directory
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

    def set_sketch_dir(cls):
        cls.__sketch_dir__ = os.getcwd()

    # Launch the IDE only
    def get_launch_ide_only(cls):
        return cls.__launch_IDE_only__

    def set_launch_ide_only(cls, new_launch_IDE_only):
        cls.__launch_IDE_only__ = new_launch_IDE_only

    launch_IDE_only = property(get_launch_ide_only, set_launch_ide_only)

    def set_launch_ide_only_default(cls):
        cls._launch_IDE_only__ = False

    # COM port
    def set_com_port_default(cls):
        cls.__com_port__ = 'COM1'

    #
    # Sets all the settings to default values
    #
    def set_default_settings(cls):
        cls.set_launch_ide_only_default()
        cls.set_compiler_dir_default()
        cls.set_sketch_dir()
        cls.set_sketch_name_default()
        cls.set_com_port_default()
        cls.set_arduino_board_default()

    #
    # Verifies
    #
    def verify_settings(cls):
        pass


    #
    # Settings file
    #
    def save_settings(cls):
        settings_parser = ConfigParser.ConfigParser()
        settings_parser.add_section('Arduino_IDE')
        settings_parser.set(
            'Arduino_IDE',
            'arduino_exec_path',
            cls.__compiler_dir__)
        settings_parser.set(
            'Arduino_IDE',
            'arduino_board',
            cls.__arduino_board_key__)
        settings_parser.set(
            'Arduino_IDE',
            'arduino_com_port',
            cls.__com_port__)
        settings_parser.add_section('Arduino_Sketch')
        settings_parser.set(
            'Arduino_Sketch',
            'sketch_name',
             cls.__sketch_name__)
        settings_parser.set(
            'Arduino_Sketch',
            'sketch_directory',
            cls.__sketch_dir__)

        # Set the path and create/overwrite the file
        settings_file = open(cls.get_settings_file_path(), 'w')
        settings_parser.write(settings_file)
        settings_file.close()

    def read_settings(cls):
        """
        Attempts to read the settings from a file and saves them to the
        member variables. If it cannot read the file it sets the variables
        to the default value.
        """
        settings_dict = cls.read_settings_file()
        if settings_dict:
            cls.__compiler_dir__ = settings_dict['arduino_exec_path']
            cls.arduino_board = settings_dict['arduino_board']
            cls.__com_port__ = settings_dict['arduino_com_port']
            cls.__sketch_name__ = settings_dict['sketch_name']
            cls.__sketch_dir__ = settings_dict['sketch_directory']
        else:
            print('Settings will be set to defaults')
            cls.set_default_settings()

        # Printing the settings to be able to easily spot issues at load
        print('Compiler directory: ' + cls.__compiler_dir__)
        print('Arduino Board Key: ' + cls.__arduino_board_key__)
        print('Arduino Board Value: ' + cls.__arduino_board_value__)
        print('COM Port: ' + cls.__com_port__)
        print('Sketch Name: ' + cls.__sketch_name__)
        print('Sketch Directory: ' + cls.__sketch_dir__)

    def read_settings_file(cls):
        """ Creates a dictionary from the settings stores in a file """
        settings_dict = {}
        settings_parser = ConfigParser.ConfigParser()
        try:
            settings_parser.read(cls.get_settings_file_path())
            settings_dict['arduino_exec_path'] =\
                settings_parser.get('Arduino_IDE', 'arduino_exec_path')
            settings_dict['arduino_board'] =\
                settings_parser.get('Arduino_IDE', 'arduino_board')
            settings_dict['arduino_com_port'] =\
                settings_parser.get('Arduino_IDE', 'arduino_com_port')
            settings_dict['sketch_name'] =\
                settings_parser.get('Arduino_Sketch', 'sketch_name')
            settings_dict['sketch_directory'] =\
                settings_parser.get('Arduino_Sketch', 'sketch_directory')
        except Exception as e:
            print("e")
            print('Could not read settings file!')
            settings_dict = None
        return settings_dict

    def delete_settings(cls):
        if os.path.exists(cls.__settings_path__):
            os.remove(cls.__settings_path__)

    def get_settings_file_path(cls):
        if not cls.__settings_path__:
            cls.__settings_path__ = os.path.join(
                os.getcwd(), cls.__settings_filename__)
        return cls.__settings_path__

    def get_board_value_from_key(cls, string_key):
        string_value = None
        for key in cls.__arduino_types__:
            if string_key is key:
                string_value = cls.__arduino_types__[key]
        return string_value

    def get_board_key_from_value(cls, string_value):
        string_key = None
        for key in cls.__arduino_types__:
            if string_value is cls.__arduino_types__[key]:
                string_key = key
        return string_key


def main():
    """ This should never be executed """
    print("This is the ServerCompilerSettings main")


if __name__ == '__main__':
    main()
