function getSketchString() {
   return Blockly.Generator.workspaceToCode('Arduino');
}

function displaySketchInAlert() {
   alert(getSketchString());
}

function sendSketchToApplet() {
   var myApp = document.applets['ArduApplet'];
   myApp.processSketch(getSketchString());
}
