class g2coreGuiBackend:
    def __init__(self):
        self.protocol = None

    def setProtocol(self, protocol):
        self.protocol = protocol

    def animate(self):
        if self.protocol != None:
            self.protocol.animate()
            while (True):
#                prefix = getLogLinePrefix()
                coreLine = self.protocol.getLine()
                if coreLine != None:
                    print " <- "+coreLine
                else:
                    break
