function sendSketchToApplet() {
   var myApp = document.applets['ArduApplet'];
   myApp.processSketch(document.getElementById("sketchTextArea").value);
   document.getElementById("sketchTextArea").value =  'TEST' + document.getElementById("sketchTextArea").value;
}

function getSketchToApplet() {
   return document.getElementById("textarea_arduino").value;
}
