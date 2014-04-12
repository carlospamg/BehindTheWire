package ArduinoAppletPackage;

import java.applet.Applet;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;


public class Settings extends Applet {

	private static final long serialVersionUID = 1L;
	private static Settings singleton = null;
	private static String compilerLocation = null;
	private static String sketchLocation = null;
	private static String compilerDefaultLocation = "C:\\IDEs\\arduino-1.5.6-r2\\arduino.exe";
	private static String sketchName = "BlocklyDuinoSketch";


	/* ********************************************************************* */
	/*  Public methods                                                       */
	/* ********************************************************************* */

	/**
	 * Constructor sets the layout 
	 */
	public Settings() {
		setCompilerAddress(readCompilerAddress());
	}


	/**
	 * Singleton instance 
	 */
	public static Settings getInstance() {
		if(singleton == null) {
			singleton = new Settings();
		}
		return singleton;
	}


	/**
	 * Getter for compilerLocation
	 */
	public String getCompilerLocation() {
		return Settings.compilerLocation;
	} 


	/**
	 * Getter for sketchName
	 */
	public String getSketchName() {
		return Settings.sketchName;
	} 


	/**
	 * Getter for sketchLocation
	 */
	public String getSketchLocation() {
		return Settings.sketchLocation;
	} 


	/**
	 * Setter for sketchLocation
	 */
	public void setSketchLocation(String newLocation) {
		Settings.sketchLocation = newLocation;
	} 


	/**
	 * Sets the internal settings for the compiler location and saves it into a text file
	 * @param location The absolute location for the compiler executable
	 */
	public void setCompilerAddress(String location) {
		Writer settingsFile = null;
		Settings.compilerLocation = location;

		try {
			/* Will create a file if it does not exist already */
			settingsFile = new BufferedWriter( new FileWriter("settings.txt") );
			settingsFile.write(location);
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if(settingsFile != null) {
					settingsFile.close();
				}
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}


	/* ********************************************************************* */
	/*  Private methods                                                      */
	/* ********************************************************************* */

	/**
	 * Reads the file settings.txt to retrieve the compiler location. If the file is not
	 * found a new one is created with the default location.
	 * @return The absolute location of the compiler executable
	 */
	private String readCompilerAddress() {
		BufferedReader settingsBR = null;
		String firstLine = null;

		try {
			/* First check if file exists and create it if not */
			File settingsFile = new File("settings.txt");
			if(!settingsFile.exists()) {
				setCompilerAddress(Settings.compilerDefaultLocation);
			}

			/* Read the first line */
			settingsBR = new BufferedReader( new FileReader("settings.txt") );
			firstLine = settingsBR.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if(settingsBR != null) {
					settingsBR.close();
				}
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}

		return firstLine;
	}
}
