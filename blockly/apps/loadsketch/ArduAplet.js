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


//
function pythonTest() {
   //alert(getSketchString());
   xml_http_post("index.html", getSketchString(), test_handle)
}

function test_button() {
    var data = document.test_form.test_text.value;           
    xml_http_post("index.html", data, test_handle)
}

function test_handle(req) {
   alert(req.responseText);
   //alert(getSketchString());
}

function xml_http_post(url, data, callback) {
    var req = false;
    try {
        // Firefox, Opera 8.0+, Safari
        req = new XMLHttpRequest();
    }
    catch (e) {
        // Internet Explorer
        try {
            req = new ActiveXObject("Msxml2.XMLHTTP");
        }
        catch (e) {
            try {
                req = new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch (e) {
                alert("Your browser does not support AJAX!");
                return false;
            }
        }
    }
    req.open("POST", url, true);
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            callback(req);
        }
    }
    req.send(data);
}