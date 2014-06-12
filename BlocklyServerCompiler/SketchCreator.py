import os


class SketchCreator():
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

    def create_sketch(self):
        arduino_sketch = open(self._sketch_dir, "w")
        arduino_sketch.write(self._sketch_default_code)
    
    #Need to figure out function polymorphism
    #def create_sketch(self, sketch_code):
    #    arduino_sketch = open(_sketch_dir, "w")
    #    arduino_sketch.write(sketch_code)
    
    def set_filename(self, newfilename):
        _sketch_filename = newfilename
        _sketch_dir = newfilename + '.ino'


if __name__ == "__main__":
    something = SketchCreator()
    something.create_sketch()
