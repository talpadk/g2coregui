#!/usr/bin/python

import os.path;
import time;
import g2coreProtocol;
import gcodeFile;

protocol = g2coreProtocol.g2coreProtocol();

pathToSend = "autosend.nc";


print "Copy the file to send to: '"+pathToSend+"' when done it will be deleted!!!"
print "Ctrl+C to stop"

if os.path.exists(pathToSend) and False:
    print "'"+pathToSend+"' already exists, aborting for human safety reasons!!!";
else:
    while True:
        #time.sleep(0.5)
        protocol.animate()
        while (True):
            coreLine = protocol.getLine()
            if coreLine != None:
                print "<- "+coreLine
            else:
                break
            
        if os.path.isfile(pathToSend):
            print "New file detected"
            gCode = gcodeFile.gcodeFile(pathToSend)
            while(True):
                #time.sleep(0.1)
                protocol.animate()
                while (True):
                    coreLine = protocol.getLine()
                    if coreLine != None:
                        print "<- "+coreLine
                    else:
                        break
                while protocol.hasFreeTxBuffers():
                    line = gCode.getLine()
                    if line == None:
                        break
                    line = '{"gc":"'+line+'"}'
                    protocol.sendLine(line)
                    print "-> "+line
            #Wait for the rest of the lines to have been send (they might still be executeing)
            while(not protocol.txIdle()):
                protocol.animate()
                coreLine = protocol.getLine()
                if coreLine != None:
                    print "<- "+coreLine
            os.remove(pathToSend)
            print "Done"
