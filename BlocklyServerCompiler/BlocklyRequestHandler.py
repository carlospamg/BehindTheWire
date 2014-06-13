import os


class BlocklyRequestHandler(object):
    """Request Handler from the BlocklyDuino app"""
    
    def launch_command_line(cls):
        command_line_command = '"C:\\IDE\\arduino-1.5.6-r2\\arduino.exe"'
        print('Command line command:\n\t' + command_line_command)
        os.system(command_line_command)


#def main():
    #do nothing yet


#if __name__ == "__main__":
#    main()
