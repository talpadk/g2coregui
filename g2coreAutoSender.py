#!/usr/bin/python
import sys
import os
scriptPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(scriptPath+"/backend")

import os.path;
import time;
import g2coreProtocol;
import gcodeFile;
from datetime import datetime

protocol = g2coreProtocol.g2coreProtocol();

pathToSend = "autosend.nc";       # Name of the file to send and delete 
protocol.MAX_TX_BUFFERS = 4       # Overwrite the default setting (4) of how many non ack'ed messages are allowed
includeDateTimeStamp = False      # If true the output will also include the date in the timestamps
burstTxEnabled = True             # If true send more than one line before serviceing the RX 
burstTxOnlyOnce = False           # Only do it once, then disable the feature
artificialDelay = 0               # Add this much artificial delay [seconds] during transmision of lines

def getLogLinePrefix():
    global protocol
    global includeDateTimeStamp
    dt = datetime.now()
    if includeDateTimeStamp:
        prefix = "%04u-%02u-%02u %02u:%02u:%02u.%03u %01u/%01u" % (dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second,int(dt.microsecond/1000),protocol.txBuffersInUse,protocol.MAX_TX_BUFFERS)
    else:
        prefix = "%02u:%02u:%02u.%03u %01u/%01u" % (dt.hour,dt.minute,dt.second,int(dt.microsecond/1000),protocol.txBuffersInUse,protocol.MAX_TX_BUFFERS)
    return prefix;
    
def receiveFunction():
    global protocol
    while (True):
        prefix = getLogLinePrefix()
        coreLine = protocol.getLine()
        if coreLine != None:
            print prefix+" <- "+coreLine
        else:
            break
        
def sendFunction():
    global protocol
    global burstTxEnabled
    while protocol.hasFreeTxBuffers():
        prefix = getLogLinePrefix()
        line = gCode.getLine()
        if line == None:
            break
        #Don't wrap G-Code i json as a work around for g2core issue #287
        #line = '{"gc":"'+line+'"}'
        protocol.sendLine(line)
        print prefix+" -> "+line
        if not burstTxEnabled:
            break
    if burstTxOnlyOnce:
        burstTxEnabled = False
        
print "Copy the file to send to: '"+pathToSend+"' when done it will be deleted!!!"
print "Ctrl+C to stop"

if os.path.exists(pathToSend) and False:
    print "'"+pathToSend+"' already exists, aborting for human safety reasons!!!";
else:
    while True:
        protocol.animate()
        receiveFunction()
            
        if os.path.isfile(pathToSend):
            print "New file detected"
            gCode = gcodeFile.gcodeFile(pathToSend)
            while(gCode.hasMoreData()):
                if (artificialDelay>0.0001):
                    time.sleep(artificialDelay)
                protocol.animate()
                receiveFunction()
                sendFunction()
                #Wait for the rest of the lines to have been send (they might still be executeing)
            while(not protocol.txIdle()):
                protocol.animate()
                receiveFunction()
            os.remove(pathToSend)
            print "Done sending"
