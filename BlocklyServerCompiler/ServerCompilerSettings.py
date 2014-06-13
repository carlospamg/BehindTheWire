import os
import ConfigParser

class ServerCompilerSettings(object):
    """ Retrieves and saves the settings for this Server Compiler """
    _singleton_instance = None
    _launch_IDE_only = False;
    _compiler_dir = "C:\arduino-1.5.6-r2\arduino.exe";
    _sketch_dir = "C:\BlocklyDuino-BtW\BlocklyDuinoSketch\BlocklyDuinoSketch.ino";
    _sketch_name = "BlocklyDuinoSketch";
    _settings_filename = "ServerCompilerSettings.ini"
    
    def __new__(cls, *args, **kwargs):
        """Creating or returning the singleton instance"""
        if not cls._singleton_instance:
            cls._singleton_instance = super(ServerCompilerSettings, cls).__new__(cls, *args, **kwargs)
        return cls._singleton_instance
    
    #
    # Getters and Setters
    #
    def get_compiler_dir(cls):
        return cls._compiler_dir
    def set_compiler_dir(cls, new_compiler_dir):
        cls._compiler_dir = new_compiler_dir
    compiler_dir = property(get_compiler_dir, set_compiler_dir)
    
    def get_sketch_dir(cls):
        return cls._sketch_dir
    def set_sketch_dir(cls, new_sketch_dir):
        cls._sketch_dir = new_sketch_dir
    sketch_dir = property(get_sketch_dir, set_sketch_dir)
    
    def get_sketch_name(cls):
        return cls._sketch_name
    def set_sketch_name(cls, new_sketch_name):
        cls._sketch_name = new_sketch_name
    sketch_name = property(get_sketch_name, set_sketch_name)
    
    def get_launch_IDE_only(cls):
        return cls._launch_IDE_only
    def set_launch_IDE_only(cls, new_launch_IDE_only):
        cls._launch_IDE_only = new_launch_IDE_only
    launch_IDE_only = property(get_launch_IDE_only, set_launch_IDE_only)

    #
    # Settings file
    #
    def save_settings(cls):
        settings_parser = ConfigParser.ConfigParser()
        settings_parser.add_section('Arduino_IDE')
        settings_parser.set('Arduino_IDE', 'Arduino_Executable_Directory', cls._compiler_dir)
        settings_parser.set('Arduino_IDE', 'Arduino_Board', cls._compiler_dir)
        settings_parser.set('Arduino_IDE', 'Arduino_COM_Port', cls._compiler_dir)
        settings_file = open(os.getcwd() + "/" + cls._settings_filename,'w')
        settings_parser.write(settings_file)
        settings_file.close()

def main():
    # Testing if singleton is working
    print("This is ")


if __name__ == '__main__':
    main()
