## BlocklyDuino for Behind the Wire
"BlocklyDuino for Behind the Wire" is a fork of [BlocklyDuino](https://github.com/gasolin/BlocklyDuino/), a web-based visual programming editor for [Arduino](http://www.arduino.cc/) that has been updated to work with the [Behind the Wire](https://github.com/carlospamg/BehindTheWire) activity.

BlocklyDuino is based on [Blockly](http://code.google.com/p/blockly/), the web-based, graphical programming editor, to provide static type language blocks and code generators for arduino programming.

"BlocklyDuino for Behind the Wire" has been designed to be used on a pc running a Python localhost HTTP server. This allows the python program to be able to compile and load the Arduino code using the [Arduino IDE](http://arduino.cc/en/main/software).

### Features

* Program an Arduino with visual drag-and-drop code blocks
* Custom blocks for programming the [Behind the Wire](https://github.com/carlospamg/BehindTheWire) kit
* Generate fully compatible arduino source code
* Load the code to an Arduino Board
* Load different examples with url parameters

### Demo

"BlocklyDuino for Behind the Wire" needs to be executed from a pc with Python and the Arduino IDE, however the original BlocklyDuino is a web tool which can be tested at
[Web](http://www.gasolin.idv.tw/public/blockly/demos/blocklyduino/index.html).

Direct links to BlocklyDuino examples and a demo video
* [demo 1](http://www.gasolin.idv.tw/public/blockly/demos/blocklyduino/index.html?url=/public/blockly/demos/blocklyduino/examples/blink.xml)
* [demo 2](http://www.gasolin.idv.tw/public/blockly/demos/blocklyduino/index.html?url=/public/blockly/demos/blocklyduino/examples/servo_potentio.xml)
* [video demo](http://www.youtube.com/watch?v=_swiyXcUvNY)

### Running BlocklyDuino for Behind the Wire

If you want to install BlocklyDuino for Behind the Wire locally, download the code from github and double click the "launch.py" file in the root directory.

#### Required Software
* [Python 2.7.x](https://www.python.org/download), probably to be ported to 3.x
* [Arduino IDE version 1.5 or higher](http://arduino.cc/en/main/software)

#### Usage 

1. Doubleclick on launch.py file, a browser window with BlocklyDuino for Behind the Wire will be launched.
2. Create an Arduino Program.
3. Click on the "Settings" button and select the Arduino IDE directory, Arduino Board to target and COM port.
4. Click on the red "Run Program" button

### ChangeLog

Check changelog [here](https://github.com/gasolin/BlocklyDuino/blob/master/CHANGELOG.txt).

This repository has been forked from [BlocklyDuino](https://github.com/gasolin/BlocklyDuino/) at the following commit :  [BlocklyDuino](https://github.com/gasolin/BlocklyDuino/commit/c1af9d8cfd46f9a9335989d529d20ba6a1d71228) == [BlocklyDuino-BtW](https://github.com/carlospamg/BlocklyDuino-BtW/commit/c1af9d8cfd46f9a9335989d529d20ba6a1d71228)

### Attributions, Original Authors and Contributors

Please refere to the [attributions](https://github.com/carlospamg/BlocklyDuino-BtW/blob/master/ATTRIBUTIONS.txt) file

### License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
