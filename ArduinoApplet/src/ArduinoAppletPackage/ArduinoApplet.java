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
	private SketchCreator sketchProject;


	/* ********************************************************************* */
	/*  Public methods                                                       */
	/* ********************************************************************* */

	/**
	 * Constructor sets the layout 
	 */
	public ArduinoApplet() throws HeadlessException {
		/* Ensure the singleton for Settings is initialised */
		settingsInstance = Settings.getInstance();

		sketchProject = new SketchCreator();

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
				/* Create default sketch project and load it */
				loadSketch(sketchProject.createArduinoSketch());
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


	/**
	 * Received data from Javascript
	 * @param dataText Text received
	 */
	public void processSketch(String jsSketchText) {
		Settings.getInstance().relaunch();
		/* Create the sketch project, then load it */
		String arduSketchLocation = sketchProject.createArduinoSketch(jsSketchText);
		loadSketch(arduSketchLocation);
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

}
