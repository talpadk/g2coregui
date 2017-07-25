import g2coreProtocol;
import time;



protocol = g2coreProtocol.g2coreProtocol();

protocol.sendLine('{"sr":n}');
protocol.sendLine('{"xfr":100}');
protocol.sendLine('{"gc":"G1 X1 F1000"}');

#protocol.sendLine('{"gc":"G1 X2 F2"}');
while(True):
    protocol.animate();
    line = protocol.getLine();
    if (line != None):
        print line;
