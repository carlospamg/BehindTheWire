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

import javax.swing.JFileChooser;
import javax.swing.filechooser.FileNameExtensionFilter;

public class Settings extends Frame {

	private static Settings singleton = null;
	
	private Label compilerLabel;
	private TextField compilerText;
	private Button compilerButton;
	
	private String compilerLocation = "C:\\IDEs\\arduino-1.5.6-r2\\arduino.exe";
	
	
	/*********************/
	/* Public operations */
	/*********************/
	
	/* Constructor: Set layout */
	public Settings() {
		this.setLayout(new FlowLayout());
		this.setTitle("Arduino Settings");
		this.setSize(600, 100);

		compilerLabel = new Label("Compiler Location: ");
		this.add(compilerLabel);
		compilerText  = new TextField("C:\\IDEs\\arduino-1.5.6-r2\\arduino.exe");
		this.add(compilerText);
		compilerButton = new Button("Set Address");
		this.add(compilerButton);
		
		/* Settings action listener */
		compilerButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				chooseCompiler();
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
	
	
	/* Singleton instance */
	public static Settings getInstance() {
		if(singleton == null) {
			singleton = new Settings();
		}
		return singleton;
	}
	
	/* Relaunch window */
	public static void relaunch() {
		singleton.setVisible(true);
	}

	/* Compiler location getter */
	public static String getCompilerLocation() {
		return singleton.compilerLocation;
	} 
	
	
	/**********************/
	/* Private operations */
	/**********************/
	
	/* Launches a file browser and updates compiler location*/
	private void chooseCompiler() {
		JFileChooser chooser = new JFileChooser();
		chooser.setFileFilter(
				new FileNameExtensionFilter("Compiler", "exe") );

		if(chooser.showOpenDialog(getParent()) == JFileChooser.APPROVE_OPTION) {
			singleton.compilerLocation = chooser.getSelectedFile().getAbsolutePath();
			singleton.compilerText.setText(getCompilerLocation());
		}
	}

}
