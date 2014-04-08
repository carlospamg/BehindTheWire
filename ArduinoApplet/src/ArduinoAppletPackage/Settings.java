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
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;

public class Settings extends Frame {

	private static final long serialVersionUID = 1L;
	private static Settings singleton = null;
	private static String compilerLocation = "C:\\IDEs\\arduino-1.5.6-r2\\arduino.exe";
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
		/* Read Settings file */
		Settings.compilerLocation = readCompilerAddress();
		
		/* Setting up the layout */
		this.setLayout(new FlowLayout());
		this.setTitle("Arduino Settings");
		this.setSize(600, 100);

		compilerLabel = new Label("Compiler Location: ");
		this.add(compilerLabel);

		compilerText  = new TextField(compilerLocation);
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
	 * 
	 * @param location
	 * @throws FileNotFoundException
	 */
	private void setCompilerAddress(String location) throws FileNotFoundException {
		singleton.compilerLocation = location;
		singleton.compilerText.setText(getCompilerLocation());
		
		PrintWriter settingsFile = new PrintWriter("settings.txt");
		settingsFile.print(location);
		settingsFile.close();
	}


	/**
	 * 
	 * @return
	 */
	private String readCompilerAddress() {
		BufferedReader br = null;
		String sCurrentLine = null;

		try {
			br = new BufferedReader( new FileReader("settings.txt") );
			sCurrentLine = br.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if(br != null) {
					br.close();
				}
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
		
		return sCurrentLine;
	}
}
