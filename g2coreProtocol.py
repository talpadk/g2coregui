import serial
import json;


class g2coreProtocol:
    MAX_RX_LENGTH=1024*100;
    RX_CUNCK_SIZE = 1024;

    serialPort = None;
    buffer = bytearray();

    
    def __init__(self):
        self.serialPort = serial.Serial(port='/dev/ttyACM0', baudrate=115000, timeout=0.01);

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
            self.buffer = self.buffer[newlinePos+1:];
            return lineAsJson;

    def sendLine(self, data):
        self.serialPort.write((data+"\n").encode('utf-8'));
