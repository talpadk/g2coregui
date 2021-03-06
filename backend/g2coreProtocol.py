import serial
import json;


class g2coreProtocol:
   
    def __init__(self):
        self.MAX_RX_LENGTH=1024*100
        self.RX_CUNCK_SIZE = 1024
        self.MAX_TX_BUFFERS = 4
        
        self.txBuffersInUse = 0
        self.lineAsJson = None
       
        self.buffer = bytearray();

        try:
            self.serialPort = serial.Serial(port='/dev/ttyACM0', baudrate=115000, timeout=0.01, rtscts=True)
        except:
            self.serialPort = None;
            print "Failed to open serial port /dev/ttyACM0";

        
    def animate(self):
        if self.serialPort != None:
            input = self.serialPort.read(self.RX_CUNCK_SIZE);
            if len(self.buffer) + len(input) > self.MAX_RX_LENGTH:
                self.buffer = bytearray();
            self.buffer = self.buffer + input;

    def getLine(self):
        newlinePos = self.buffer.find("\n")
        if newlinePos == -1:
            return None;
        else:
            self.lineAsJson = None;
            line = self.buffer[0:newlinePos].decode('utf-8');
            try:
                self.lineAsJson = json.loads(line);
            except:
                {}
            if self.lineAsJson != None:
                if 'f' in self.lineAsJson:
                    footer = self.lineAsJson['f'];
                if 'r' in self.lineAsJson:
                    self.txBuffersInUse -= 1
                    if self.txBuffersInUse<0:
                        self.txBuffersInUse=0
            self.buffer = self.buffer[newlinePos+1:];
            #print "on rx "+str(self.txBuffersInUse)
            return line;

    def getLastLineAsJson(self):
        return self.lineAsJson

    def sendLine(self, data):
        if self.serialPort != None:
            self.serialPort.write((data+"\n").encode('utf-8'));
            self.txBuffersInUse += 1
            #print "on tx "+str(self.txBuffersInUse)

    #Method for sending the special single character commands that don't generate a response    
    def sendSpecialCommand(self, data):
        if self.serialPort != None:
            self.serialPort.write((data+"\n").encode('utf-8'));
        
    def hasFreeTxBuffers(self):
        if self.txBuffersInUse < self.MAX_TX_BUFFERS:
            return True
        else:
            return False
        
    def txIdle(self):
        if self.txBuffersInUse==0:
            return True
        else:
            return False
