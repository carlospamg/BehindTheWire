import os
import ConfigParser

class ServerCompilerSettings(object):
    """
    Retrieves and saves the settings for this Server Compiler
    """
    
    # Designed to be immutable variables
    _singleton_instance = None
    _settings_filename = "ServerCompilerSettings.ini"
    
    # Settings with getters and setters
    _launch_IDE_only = False
    _compiler_dir = "C:\\IDEs\\arduino-1.5.6-r2\\arduino.exe"
    _sketch_dir = "G:\\GE\\CSF\\git\\BlocklyDuino"
    _sketch_name = "BlocklyDuinoSketch"
    
    #
    # Singleton creator 
    #
    def __new__(cls, *args, **kwargs):
        """Creating or returning the singleton instance"""
        if not cls._singleton_instance:
            cls._singleton_instance = super(ServerCompilerSettings, cls).__new__(cls, *args, **kwargs)
            cls._sketch_dir = os.getcwd()
        return cls._singleton_instance
    
    #
    # Getters and Setters
    #
    def get_compiler_dir(cls):
        return cls._compiler_dir
    def set_compiler_dir(cls, new_compiler_dir):
        if os.path.exists(new_compiler_dir):
            cls._compiler_dir = new_compiler_dir
    compiler_dir = property(get_compiler_dir, set_compiler_dir)
    
    def get_sketch_dir(cls):
        return cls._sketch_dir
    def set_sketch_dir(cls, new_sketch_dir):
        if os.path.exists(new_sketch_dir):
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
        settings_parser.add_section('Arduino_Sketch')
        settings_parser.set('Arduino_Sketch', 'Sketch_Name', cls._sketch_name)
        settings_parser.set('Arduino_Sketch', 'Sketch_Directory', cls._sketch_dir)
        settings_file = open( os.path.join( os.getcwd(),
                                           cls._settings_filename),'w')
        settings_parser.write(settings_file)
        settings_file.close()

def main():
    # This should never be executed
    print("This is the ServerCompilerSettings main")


if __name__ == '__main__':
    main()
