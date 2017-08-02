class g2coreGuiBackendDRO:

    def __init__(self):
        self.changes = True
        self.positionInformation = {}
        
    def getValueAsText(self, name):
        name = "pos"+name
        if name in self.positionInformation:
            return str(self.positionInformation[name])
        else:
            return "?"

    def hasChanges(self):
        value = self.changes
        self.changes = False
        return value

    def updateValue(self, status, name):
        if name in status:
            self.positionInformation[name] = status[name]
            self.changes = True
                       
    def animate(self, data):
        status = None
        
        if "sr" in data:
            status = data["sr"]
        elif "r" in data:
            if "sr" in data["r"]:
                status = data["r"]["sr"]
        if status != None:
            self.updateValue(status, "posx")
            self.updateValue(status, "posy")
            self.updateValue(status, "posz")
            self.updateValue(status, "posa")
            self.updateValue(status, "posb")
            self.updateValue(status, "posc")
                    
