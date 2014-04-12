package ArduinoAppletPackage;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;

public class SketchCreator {

	private String sketchCode = null;


	/* ********************************************************************* */
	/*  Public methods                                                       */
	/* ********************************************************************* */

	/**
	 *  Public Constructor creates default Arduino Sketch
	 */
	public SketchCreator() {
		createArduinoSketch();
	}


	/**
	 * Public Constructor
	 * @param sketchText Code for the sketch to be created
	 */
	public SketchCreator(String sketchText) {
		createArduinoSketch(sketchText);
	}


	/**
	 * Creates default Arduino Sketch
	 * @return location of the Sketch
	 */
	public void createArduinoSketch() {
		createArduinoSketch(this.sketchCode);
	}


	/**
	 * Creates an Arduino Sketch with the code send in an argument
	 * @param sketchText Code for the Arduino Sketch
	 * @return location of the Sketch
	 */
	public void createArduinoSketch(String sketchText) {
		File directory;
		File sketchFile;
		String sketchFileName = Settings.getInstance().getSketchName();
		String location = null;

		/* Prepare sketch project string */
		StringBuilder sketchProject = new StringBuilder();
		sketchProject.append(sketchFileName);
		sketchProject.append("/");
		sketchProject.append(sketchFileName);
		sketchProject.append(".ino");

		/* Set string with code */
		if(sketchText == null) {
			this.sketchCode = defaultSketchCode();
		} else {
			this.sketchCode = sketchText;
		}

		/* Create sketch */
		try {
			directory = new File(sketchFileName);
			directory.mkdir();
			sketchFile = new File(sketchProject.toString());
			setSketchContents(sketchFile, this.sketchCode);
			location = sketchFile.getAbsoluteFile().toString();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		/* Set the full sketch path into the Settings class */
		Settings.getInstance().setSketchLocation(location);
		//System.out.println("s: " + location);
	}


	/* ********************************************************************* */
	/*  Private methods                                                      */
	/* ********************************************************************* */

	/** 
	 * Creates a default Sketch code
	 * @return Default Arduino code
	 */
	private String defaultSketchCode() {
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
	 * Sets the code of a Sketch file and closes the file.
	 * @param aFile file instance of Sketch
	 * @param aContents Sketch code
	 */
	private void setSketchContents(File aFile, String aContents) throws IOException {
		if(aFile == null) {
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
