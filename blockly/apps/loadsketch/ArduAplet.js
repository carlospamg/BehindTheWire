function sendSketchToApplet() {
   var myApp = document.applets['ArduApplet'];
   myApp.processSketch(document.getElementById("sketchTextArea").value);
   document.getElementById("sketchTextArea").value =  'TEST' + document.getElementById("sketchTextArea").value;
}

function getSketchToApplet() {
   return Blockly.Generator.workspaceToCode('Arduino');
}

function displaySketchInAlert() {
   var mySketch = Blockly.Generator.workspaceToCode('Arduino');
alert(mySketch);
}