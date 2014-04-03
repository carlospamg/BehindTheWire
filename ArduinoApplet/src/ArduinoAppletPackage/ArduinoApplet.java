package ArduinoAppletPackage;

import java.applet.Applet;
import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;


public class ArduinoApplet extends Applet {
	private static final long serialVersionUID = 1L;
	
	private Button buttonLoad;
	private Button buttonSettings;
	private Settings settingsInstance;
	
	
	/* ********************************************************************* */
	/*  Public methods                                                       */
	/* ********************************************************************* */
	
	/**
	 * Constructor sets the layout 
	 */
	public ArduinoApplet() throws HeadlessException {
		/* Ensure the singleton for Settings is initialised */
		settingsInstance = Settings.getInstance();
		
		/* Set layout */
		this.setLayout(new FlowLayout());
		buttonLoad = new Button("Load to Arduino");
		this.add(buttonLoad);
		buttonSettings = new Button("Settings");
		this.add(buttonSettings);
		
		/* Load Sketch action listener */
		buttonLoad.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				/* Create the sketch project, then load it */
				String arduSketchLocation = createArduinoSketch(Settings.getInstance().getSketchName());
				loadSketch(arduSketchLocation);
			}
		});
		
		/* Settings action listener */
		buttonSettings.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				Settings.getInstance().relaunch();
			}
		});
	}

	/* ********************************************************************* */
	/*  Private methods                                                      */
	/* ********************************************************************* */
	
	/**
	 *  Launches the command line to load Arduino Sketch
	 */
	private void loadSketch(String sketchLocation) {
		Process pr;
		
		/* Build and load by command line */
		StringBuilder arduinoCommands = new StringBuilder();
		arduinoCommands.append(settingsInstance.getCompilerLocation());
		arduinoCommands.append(" --upload ");
		//TODO: maybe add arduino settings to settings class, change manually for now
		arduinoCommands.append("--board arduino:avr:diecimila:cpu=atmega168 ");
		arduinoCommands.append("--verbose ");
		arduinoCommands.append(sketchLocation);

		try {
			/* Launch command line and capture stream*/
			pr = Runtime.getRuntime().exec("cmd /c start cmd.exe /K \"" +
					arduinoCommands.toString() + " && exit\" ");
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	

	/**
	 *  Reads text from the clipboard and writes it to an Arduino Sketch
	 */
	private static String createArduinoSketch(String filename){
		File directory;
		File sketchFile;
		String toReturn = null;
		
		/* Prepare sketch project string */
		StringBuilder sketchProject = new StringBuilder();
		sketchProject.append(filename);
		sketchProject.append("/");
		sketchProject.append(filename);
		sketchProject.append(".ino");
		
		/* Retrieve string for code */
		String sketchText = readSketch();

		/* Create sketch */
		try {
			directory = new File(filename);
			directory.mkdir();
			sketchFile = new File(sketchProject.toString());
			setFileContents(sketchFile, sketchText);
			toReturn = sketchFile.getAbsoluteFile().toString();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		return toReturn;
	}
	
	/**
	 *  Reads from the clipboard and returns string
	 */
	private static String readSketch() {
		StringBuilder sketchCode = new StringBuilder();
		sketchCode.append("int led = 13;\r\n");
		sketchCode.append("void setup() {\r\n"); 
		sketchCode.append("  pinMode(led, OUTPUT);\r\n");
		sketchCode.append("}\r\n");
		sketchCode.append("void loop() {\r\n");
		sketchCode.append("  digitalWrite(led, HIGH);\r\n");
		sketchCode.append("  delay(1000);\r\n");
		sketchCode.append("  digitalWrite(led, LOW);\r\n");
		sketchCode.append("  delay(1000);\r\n");
		sketchCode.append("}\r\n");

		return sketchCode.toString();
	}

	/**
	 *  Adds string to a file instance, then closes it 
	 */
	private static void setFileContents(File aFile, String aContents) throws IOException {
		if (aFile == null) {
			throw new IllegalArgumentException("File should not be null.");
		}
		
		/* Create if it doesn't exits */
		if (!aFile.exists()) {
			try {
				aFile.createNewFile();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		if (!aFile.isFile()) {
			throw new IllegalArgumentException("Should not be a directory: " + aFile);
		}
		if (!aFile.canWrite()) {
			throw new IllegalArgumentException("File cannot be written: " + aFile);
		}
		
		/* Write to file (FileWriter always assumes default encoding is OK!) */
		Writer output = new BufferedWriter(new FileWriter(aFile));
		try {
			output.write(aContents);
		} finally {
			output.close();
		}
	}

}
