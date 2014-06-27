import os
from ServerCompilerSettings import ServerCompilerSettings

class SketchCreator(object):
    """
    Creates an Arduino Sketch
    """
    
    #This is probably not the best way to create this string, will revisit
    _sketch_default_code = """int led = 13;
void setup() {
  pinMode(led, OUTPUT);
}
void loop() {
  digitalWrite(led, HIGH);
  delay(1000);
  digitalWrite(led, LOW);
  delay(1000);
}"""
    
    #
    # Constructor
    #
    #def __init__(self):
    
    
    #
    # Creating files
    #
    def create_sketch(self, sketch_code=None):
        """
        Creates the ardunino sketch with either the default blinky
        code or the code defined in the input parameter
        """
        sketch_path = self.build_sketch_path()
        if isinstance(sketch_code, str) and sketch_code:
            code_to_write = sketch_code
        else:
            code_to_write = self._sketch_default_code
        try:
            arduino_sketch = open(sketch_path, 'w')
            arduino_sketch.write(code_to_write)
            arduino_sketch.close()
        except:
            sketch_path = None
        
        return sketch_path
    
    #
    # File and directories settings
    #
    def build_sketch_path(self):
        """
        If a valid directory is saved in the settings, it creates the Arduino
        folder if required and returns a string pointing to the sketch path
        """
        sketch_name = ServerCompilerSettings().sketch_name
        sketch_directory = ServerCompilerSettings().sketch_dir
        sketch_path = None
        
        if os.path.exists(sketch_directory):
            sketch_path = os.path.join(sketch_directory, sketch_name)
            if not os.path.exists(sketch_path):
                os.makedirs(sketch_path)
            sketch_path = os.path.join(sketch_path, sketch_name + '.ino')
        
        return sketch_path 


def main():
    # This should never be executed
    print("This is the SketchCreator main")


if __name__ == "__main__":
    main()
