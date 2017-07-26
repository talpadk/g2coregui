import g2coreGuiBackendLogHistory

class g2coreGuiBackend:
    def __init__(self, application):
        self.protocol = None
        self.application = application
        self.userCommandQueue = []
        self.logHistory = g2coreGuiBackendLogHistory.g2coreGuiBackendLogHistory()
        
    def setProtocol(self, protocol):
        self.protocol = protocol

    def animate(self):
        if self.protocol != None:
            self.protocol.animate()
            while (True):
#                prefix = getLogLinePrefix()
                coreLine = self.protocol.getLine()
                if coreLine != None:
                    self.logHistory.addLine(0, coreLine)
                else:
                    break
                
            moreDataToSend = True
            while moreDataToSend:
                if self.protocol.hasFreeTxBuffers:
                    command = None
                    if len(self.userCommandQueue)>0:
                        command = self.userCommandQueue.pop(0)
                    if command != None:
                        self.protocol.sendLine(command)
                        self.logHistory.addLine(1, command)
                    else:
                        moreDataToSend = False
                else:
                    moreDataToSend = False
                
    def appendUserCommandToQueue(self, command):
        self.userCommandQueue.append(command)
