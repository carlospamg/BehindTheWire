function send_sketch_to_server() {
   //alert(getSketchString());
   xml_http_post("index.html", getSketchString(), server_callback)
}


function server_callback(req) {
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


function open_settings() {
   var settings_file_dir = "../loadsketch/ArduServerCompilerSettings.html";

   var settingsPopupWindow = window.open(
      settings_file_dir,
      'popUpWindow',
      'height=150,width=500,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes');

   if (settingsPopupWindow.focus) {
      settingsPopupWindow.focus()
   }

   return false;
}