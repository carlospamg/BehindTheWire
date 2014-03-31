import java.applet.Applet;
import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.HeadlessException;
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.Transferable;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;


public class ArduinoApplet extends Applet implements ActionListener {
    Button button_load = new Button("Load to Arduino");
	
    /* Constructor: Place the button */
	public ArduinoApplet() throws HeadlessException {
		this.setLayout(new FlowLayout());
		this.add(button_load);
		button_load.addActionListener(this);
	}

	/* Action Listener: Execute command line commands */
	@Override
	public void actionPerformed(ActionEvent arg0) {
		Process pr;
		OutputStream pr_os;
		createArduinoSketch("test2.ino");
		
		try {
			/* Launch command line and capture stream*/
			pr = Runtime.getRuntime().exec("cmd /c start cmd.exe /K \"BuildAndLoad.bat && exit\" ");
			pr_os = pr.getOutputStream();
			 
			/* Write commands */
			pr_os.write("dir /r/n".getBytes());
			pr_os.flush();
			pr_os.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	
	
	
	/* Reads text from the clipboard and writes it to an Arduino Sketch */
	private static void createArduinoSketch(String filename){
	    String clipText = readClipboard();
        try {
        	File texfile = new File(filename);
            setContents(texfile, clipText);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
	}
	
	/* Reads from the clipboard and returns string */
	private static String readClipboard() {
	    /* Get Clipboard and check if empty*/
	    Clipboard systemClipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
    	//FIXME starts: Temp code to put something in the clipboard
	    	StringSelection selection = new StringSelection("arduino code");
	    	systemClipboard.setContents(selection, selection);
    	//FIXME end
	    Transferable clipboardContents = systemClipboard.getContents(null);
	    if (clipboardContents.equals(null)) {
	    	return ("Clipboard is empty.");
	    } 

	    try {
	    	/* See if DataFlavor of DataFlavor.stringFlavor is supported */
	        if (clipboardContents.isDataFlavorSupported(DataFlavor.stringFlavor)) {
	        	String clipboardText = (String)clipboardContents.getTransferData(DataFlavor.stringFlavor);
	            return clipboardText;
	        }
	    } catch (UnsupportedFlavorException ufe) {
	        ufe.printStackTrace();
	    } catch (IOException ioe) {
	        ioe.printStackTrace();
	    }

	    return null;
	}

    /* Adds string to a file instance, then closes it */
	static private void setContents(File aFile, String aContents) throws IOException {

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
