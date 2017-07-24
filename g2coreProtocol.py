import serial
import json;


class g2coreProtocol:
   
    def __init__(self):
        self.MAX_RX_LENGTH=1024*100
        self.RX_CUNCK_SIZE = 1024
        self.MAX_TX_BUFFERS = 1
        
        self.txBuffersInUse = 0
       
        self.buffer = bytearray();
        self.serialPort = serial.Serial(port='/dev/ttyACM0', baudrate=115000, timeout=0.01, rtscts=True);

    def animate(self):
        input = self.serialPort.read(self.RX_CUNCK_SIZE);
        if len(self.buffer) + len(input) > self.MAX_RX_LENGTH:
            self.buffer = bytearray();
        self.buffer = self.buffer + input;

    def getLine(self):
        newlinePos = self.buffer.find("\n")
        if newlinePos == -1:
            return None;
        else:
            lineAsJson = None;
            line = self.buffer[0:newlinePos].decode('utf-8');
            try:
                lineAsJson = json.loads(line);
            except:
                {}
            if lineAsJson != None:
                if 'f' in lineAsJson:
                    footer = lineAsJson['f'];
                if 'r' in lineAsJson:
                    self.txBuffersInUse -= 1
                    if self.txBuffersInUse<0:
                        self.txBuffersInUse=0
            self.buffer = self.buffer[newlinePos+1:];
            #print "on rx "+str(self.txBuffersInUse)
            return line;

    def sendLine(self, data):
        self.serialPort.write((data+"\n").encode('utf-8'));
        self.txBuffersInUse += 1
        #print "on tx "+str(self.txBuffersInUse)

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
