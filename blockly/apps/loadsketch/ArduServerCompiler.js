/////////////////////////////
// Communicate with Server //
/////////////////////////////
function simple_ajax_post_form(url, params, callback) {
   var request = false;
   try {
      // Firefox, Chrome, IE7+, Opera, Safari
      request = new XMLHttpRequest();
   }
   catch (e) {
      // IE6-
      try {
         request = new ActiveXObject("Msxml2.XMLHTTP");
      }
      catch (e) {
         try {
            request = new ActiveXObject("Microsoft.XMLHTTP");
         }
         catch (e) {
            alert("Your browser does not support AJAX!");
            return false;
         }
      }
   }
   request.open("POST", url, true);
   //TODO: Look for a non-deprecated content-type
   request.setRequestHeader("Content-type","application/x-www-form-urlencoded");
   request.setRequestHeader("Content-length", params.length);
   request.setRequestHeader("Connection", "close");
   
   request.onreadystatechange = function() {
      if ( (request.readyState == 4) && (request.status == 200) ) {
         callback(request.responseText);
      }
   }
   request.send(params);
}


function simple_ajax_post_plain(url, data, callback) {
   var request = false;
   try {
      // Firefox, Chrome, IE7+, Opera, Safari
      request = new XMLHttpRequest();
   }
   catch (e) {
      // IE6-
      try {
         request = new ActiveXObject("Msxml2.XMLHTTP");
      }
      catch (e) {
         try {
            request = new ActiveXObject("Microsoft.XMLHTTP");
         }
         catch (e) {
            alert("Your browser does not support AJAX!");
            return false;
         }
      }
   }
   request.open("POST", url, true);
   //TODO: Look for a non-deprecated content-type
   request.setRequestHeader("Content-type","text/plain");
   request.setRequestHeader("Content-length", data.length);
   request.setRequestHeader("Connection", "close");
   
   request.onreadystatechange = function() {
      if ( (request.readyState == 4) && (request.status == 200) ) {
         callback(request.responseText);
      }
   }
   request.send(data);
}

//////////////
// Settings //
//////////////
function open_settings() {
   var settings_file_dir = "../loadsketch/ArduServerCompilerSettings.html";
   var settingsPopupWindow = window.open(
      settings_file_dir,
      'popUpWindow',
      'height=150,width=400,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes');
   if (settingsPopupWindow.focus) {
      settingsPopupWindow.focus()
   }
   return false;
}


function click_element(elementToClick) {
   document.getElementById(elementToClick).click();
}


function set_compiler_location(fileInput, textField) {
   document.getElementById(textField).value = fileInput.value;
   //TODO: Add AJAX code to set compiler location on server settings
}

/* 3 functions to get and set compiler location */
function get_compiler_location() {
   simple_ajax_post_form("ArduServerCompilerSettings.html", "compiler=get&something=else", set_compiler_location_html)
}

function request_new_compiler_location() {
  simple_ajax_post_form("ArduServerCompilerSettings.html", "compiler=set&something=else", set_compiler_location_html)
}

function set_compiler_location_html(newLocation) {
  document.getElementById('compilerLocationTextField').value = newLocation;
}

/* 3 functions to get and set sketch location */
function get_sketch_location() {
   simple_ajax_post_form("ArduServerCompilerSettings.html", "sketch=get", set_sketch_location_html)
}

function request_new_sketch_location() {
  simple_ajax_post_form("ArduServerCompilerSettings.html", "sketch=set", set_sketch_location_html)
}

function set_sketch_location_html(newLocation) {
  document.getElementById('sketchLocationTextField').value = newLocation;
}


/* 3 functions to get and set launch ide only checkbox */
function get_ide_only() {
   simple_ajax_post_form("ArduServerCompilerSettings.html", "ideOnly=get", set_ide_only_html)
}

function set_ide_only() {
  // Determine state of checkbox and set value to send
  if(document.getElementById('onlyIde').checked) {
    new_value = "True";
  } else {
    new_value = "False";
  }
  // POST send
  simple_ajax_post_form("ArduServerCompilerSettings.html", "ideOnly=set&value=" + new_value, set_ide_only_html)
}

function set_ide_only_html(newBooleanString) {
  if(newBooleanString == 'True') {
    new_value = true;
  } else {
    new_value = false;
  }
  document.getElementById('onlyIde').checked = new_value;
}


//////////////////////////
// Load and Run Program //
//////////////////////////
function getSketchCode() {
   return Blockly.Generator.workspaceToCode('Arduino');
}


function send_sketch_to_server() {
   //alert(getSketchString());
   simple_ajax_post_plain("index.html", getSketchCode(), server_callback)
}


function server_callback(response) {
   alert(response);
}
