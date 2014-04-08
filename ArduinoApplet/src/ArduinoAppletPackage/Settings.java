package ArduinoAppletPackage;

import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;

public class Settings extends Frame {

	private static final long serialVersionUID = 1L;
	private static Settings singleton = null;
	private static String compilerLocation = null;
	private static String compilerDefaultLocation = "C:\\IDEs\\arduino-1.5.6-r2\\arduino.exe";
	private static String sketchName = "BlocklyDuinoSketch";

	private Label compilerLabel;
	private TextField compilerText;
	private Button compilerButton;
	private Button closeButton;


	/* ********************************************************************* */
	/*  Public methods                                                       */
	/* ********************************************************************* */

	/**
	 * Constructor sets the layout 
	 */
	public Settings() {
		/* Setting up the layout */
		this.setLayout(new FlowLayout());
		this.setTitle("Arduino Settings");
		this.setSize(600, 100);

		compilerLabel = new Label("Compiler Location: ");
		this.add(compilerLabel);

		compilerText  = new TextField(compilerDefaultLocation);
		compilerText.setSize(200, 25);
		this.add(compilerText);

		compilerButton = new Button("Set Location");
		this.add(compilerButton);

		closeButton = new Button("Close");
		this.add(closeButton);

		/* Settings action listener */
		compilerButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				chooseCompiler();
			}
		});

		/* Close button action listener */
		closeButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				dispose();
			}
		});

		/* Implement close function */
		this.addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent we) {
				dispose();
			}
		});

		/* Read Settings file */
		Settings.compilerLocation = readCompilerAddress();

		/* Do not draw on construction */
		//this.setVisible(true);
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
	 * Relaunches window 
	 */
	public void relaunch() {
		getInstance().setVisible(true);
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


	/* ********************************************************************* */
	/*  Private methods                                                      */
	/* ********************************************************************* */

	/**
	 * Launches a file browser and updates compiler location
	 */
	private void chooseCompiler() {
		JFileChooser chooser = new JFileChooser();
		chooser.setFileFilter( new FileNameExtensionFilter("Compiler", "exe") );

		if(chooser.showOpenDialog(getParent()) == JFileChooser.APPROVE_OPTION) {
			try {
				setCompilerAddress(chooser.getSelectedFile().getAbsolutePath());
			} catch(FileNotFoundException e) {
				e.printStackTrace();
			}
		}
	}


	/**
	 * Sets the internal settings for the compiler location and saves it into a text file
	 * @param location The absolute location for the compiler executable
	 */
	private void setCompilerAddress(String location) throws FileNotFoundException {
		Writer settingsFile = null;
		Settings.compilerLocation = location;
		this.compilerText.setText(Settings.compilerLocation);
		
		try {
			/* Will create a file if it does not exist already */
			settingsFile = new BufferedWriter( new FileWriter("settings.txt") );
			settingsFile.write(location);
		} catch (IOException e) {
			// TODO Auto-generated catch block
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
