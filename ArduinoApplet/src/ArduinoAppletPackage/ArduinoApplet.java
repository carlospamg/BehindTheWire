package ArduinoAppletPackage;

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.FileDialog;
import java.awt.FlowLayout;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;

import javax.swing.JApplet;
import javax.swing.JFrame;
import javax.swing.JPanel;

import netscape.javascript.JSObject;


public class ArduinoApplet extends JApplet {
	private static final long serialVersionUID = 1L;

	private JPanel cards;
	private Button buttonLoad;
	private Button buttonSettings;
	private Settings settingsInstance;
	private SketchCreator sketchProject;
	private Label compilerLabel;
	private TextField compilerText;
	private Button compilerButton;
	private Boolean isApplet = true;


	/* ********************************************************************* */
	/*  Public methods                                                       */
	/* ********************************************************************* */

	/**
	 * Constructor unused for applet, init function to be called instead
	 */
	public ArduinoApplet() {
	
	}


	/**
	 * Applet initialisation
	 */
	public void init() {
		/* Initialise objects */
		settingsInstance = Settings.getInstance();
		sketchProject = new SketchCreator();

		/* Set layout */
		try {
			javax.swing.SwingUtilities.invokeAndWait(new Runnable() {
				public void run() {
					createGui();
				}
			});
		} catch (Exception e) {
			System.err.println("createGui didn't complete successfully!");
		}
	}


	/**
	 * Receives data from Javascript, creates and loads sketch into Arduino
	 * @param dataText Text received
	 */
	public void processSketch(String jsSketchText) {
		/* Create the sketch project, then load it */
		sketchProject.createArduinoSketch(jsSketchText);
		loadSketch();
	}


	/**
	 * Configures this class to not run as a JAR file
	 */
	public void runAsJar() {
		isApplet = false;
	}

	/* ********************************************************************* */
	/*  Private methods                                                      */
	/* ********************************************************************* */

	/**
	 * Sets the layout of the Applet GUI
	 */
	private void createGui() {
		Container pane = getContentPane();

		/* Components always visible */
		JPanel permanentPanel= new JPanel( new FlowLayout(FlowLayout.RIGHT) );
		buttonLoad = new Button("Load to Arduino");
		permanentPanel.add(buttonLoad);
		permanentPanel.setBackground(Color.WHITE);

		buttonSettings = new Button("Settings");
		permanentPanel.add(buttonSettings);

		/* Create the "cards", for now one has nothing */
		JPanel appletCardNothing = new JPanel();
		appletCardNothing.setBackground(Color.WHITE);
		JPanel appletCardSettings = new JPanel();
		appletCardSettings.setBackground(Color.WHITE);
		
		compilerLabel = new Label("Compiler Location: ");
		appletCardSettings.add(compilerLabel);

		compilerText  = new TextField(Settings.getInstance().getCompilerLocation());
		compilerText.setSize(200, 25);
		appletCardSettings.add(compilerText);

		compilerButton = new Button("Set Location");
		appletCardSettings.add(compilerButton);

		/* Create the panel to contain the cards */
		cards = new JPanel(new CardLayout());
		cards.add(appletCardNothing, "appletCardNothing");
		cards.add(appletCardSettings, "appletCardSettings");

		pane.add(cards, BorderLayout.CENTER);
		pane.add(permanentPanel, BorderLayout.PAGE_END);

		/* **************** */
		/* Action Listeners */
		/* **************** */
		/* Load Sketch action listener */
		buttonLoad.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				/* Get the sketch code, create the project and load it */
				if(isApplet == true ) {
					/* Sketch code from Html */
					sketchProject.createArduinoSketch(getSketch());
				} else {
					/* Default sketch code */
					sketchProject.createArduinoSketch();
				}
				loadSketch();
			}
		});

		/* Show Settings action listener */
		buttonSettings.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				((CardLayout)cards.getLayout()).next(cards);
			}
		});

		/* Select Compiler Action listener*/
		compilerButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				chooseCompiler();
			}
		});
	}


	/**
	 * Executes a Javascript function in the parent html website that returns the sketch code
	 * @return Sketch code from html/javascript
	 */
	private String getSketch() {
		JSObject win = JSObject.getWindow(this);
		return (String)win.eval("getSketchToApplet();");
	}


	/**
	 * Launches a file browser and updates compiler location
	 */
	private void chooseCompiler() {
		FileDialog fd = new FileDialog(new JFrame(), "Choose the Arduino IDE executable", FileDialog.LOAD);
		fd.setDirectory("C:\\");
		fd.setFile("*.exe");
		fd.setVisible(true);
		StringBuilder compilerFullPath = new StringBuilder();
		compilerFullPath.append(fd.getDirectory());
		compilerFullPath.append(fd.getFile());
		if (fd.getFile() == null) {
			compilerText.setText("Select File");
		} else {
			compilerText.setText(compilerFullPath.toString());
			settingsInstance.setCompilerAddress(compilerFullPath.toString());
		}
	}


	/**
	 *  Launches the command line to load the Arduino Sketch
	 */
	private void loadSketch() {
		/* Build and load by command line */
		StringBuilder arduinoCommands = new StringBuilder();
		
		/* First the command line text */
		arduinoCommands.append("cmd start cmd.exe /K \"");
		
		/* Now the arduino commands */
		arduinoCommands.append(settingsInstance.getCompilerLocation());
		arduinoCommands.append(" --upload ");
		//TODO: maybe add arduino settings to settings class, change manually for now
		arduinoCommands.append("--board arduino:avr:diecimila:cpu=atmega168 ");
		arduinoCommands.append("--verbose \"");
		arduinoCommands.append(Settings.getInstance().getSketchLocation());
		
		/* Finish with an exit to close the command prompt */
		arduinoCommands.append("\" && exit\" ");
		try {
			/* Launch command line and capture stream*/
			Runtime.getRuntime().exec(arduinoCommands.toString());
			System.out.println(arduinoCommands.toString());
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
