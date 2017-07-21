import serial;


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
        if input.find("\n")!=-1:
            print self.buffer;




protocol = g2coreProtocol();

while(True):
    protocol.animate();
            
