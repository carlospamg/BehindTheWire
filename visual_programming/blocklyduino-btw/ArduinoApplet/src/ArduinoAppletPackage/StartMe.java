package ArduinoAppletPackage;
 
public class StartMe{

	public static void main(String [] args) {
		// create an object of type CaesarCode which is the main applet class
		ArduinoApplet theApplet = new ArduinoApplet();
		theApplet.init();     // invoke the applet's init() method
		theApplet.runAsJar(); // configure it to run as java app
		theApplet.start();    // starts the applet, not implemented

		// Create a window (JFrame) and make applet the content pane.
		javax.swing.JFrame window = new javax.swing.JFrame("Arduino Applet");
		window.setContentPane(theApplet);
		window.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);
		window.pack();              // Arrange the components.
		window.setVisible(true);    // Make the window visible.
	}

}