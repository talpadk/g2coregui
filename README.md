![Screen shot of g2coreGui](https://raw.githubusercontent.com/wiki/talpadk/g2coregui/images/g2coreGUI.png)
## About
This python code is intended to send commands and g-code to a controller running [g2core](https://github.com/synthetos/g2/wiki).

It consists of two programs:

* g2coreGUI.py a work in progress graphical user interface
* g2coreAutoSender.py a simple command line utility for sending c-code, you probably want to use the gui instead.

The UI uses the [wxWidgets cross platform gui library](https://www.wxwidgets.org/).  
The code is intended to be cross platfom and is capable of function just fine offline / without an Internet connection.  
However it is developed and tested under Linux and things like the serial port name is still hard coded to the Linux name.

## Usage

### g2coreGUI
Start g2coreGUI.py from the source folder.  
g2coreGUI is hard coded to use /dev/ttyACM0 for the connection to the g2core, it still has a log way to go, but is has some basic functionality done

### g2coreAutoSender
When ./g2coreAutoSender.py is started it opens an connection to /dev/ttyACM0 (currently hardcoded) and waits for a file named autosend.nc to appear, when it is found it is send to the g2core and when done **autosend.nc will be DELETED!!**

eg.

Run:
>./g2coreAutoSender.py

To send a single line of g-code
>echo > autosend.nc "G1 X3 F1000"

To send a entire file
>cp myGCodeFile autosend.nc