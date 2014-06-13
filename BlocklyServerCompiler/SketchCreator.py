import os

class SketchCreator(object):
    """ Creates an Arduino Sketch """
    
    _sketch_filename = 'BlocklyDuinoSketch'
    _sketch_dir = 'BlocklyDuinoSketch.ino'
    
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

    def create_sketch(self, sketch_code=None):
        """ creates the ardunino sketch with either the default blinky """
        """ code or the code defined in the input parameter            """
        arduino_sketch = open(self._sketch_dir, "w")
        if isinstance(sketch_code, str) and sketch_code:
            arduino_sketch.write(sketch_code)
        else:
            arduino_sketch.write(self._sketch_default_code)
    
    def set_filename(self, newfilename):
        _sketch_filename = newfilename
        _sketch_dir = newfilename + '.ino'


def main():
    something = SketchCreator()
    something.create_sketch()


if __name__ == "__main__":
    main()
