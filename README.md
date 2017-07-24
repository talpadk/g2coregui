## About
This python code is intended to send commands and g-code to a controller running g2core.

It may or may not evolve into a wxpython based UI for g2core

Currently it has a **bug** that prevents it from sending "large" files to the g2core, as the g2core keeps requesting more data and eventually overflows.

## Usage
When ./g2coreAutoSender.py is started it opens an connection to /dev/ttyACM0 (currently hardcoded) and waits for a file named autosend.nc to appear, when it is found it is send to the g2core and when done **autosend.nc will be DELETED!!**

eg.

Run:
>./g2coreAutoSender.py

To send a single line of g-code
>echo > autosend.nc "G1 X3 F1000"

To send a entire file
>cp myGCodeFile autosend.nc