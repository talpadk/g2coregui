class g2coreGuiBackendLogHistory:
    def __init__(self):
        self.lines = []
        self.changes = False
        
    def addLine(self, direction, line):
        line = [direction, line]
        self.lines.append(line)
        self.changes = True

    def getLastNLinesAsText(self, number):
        end = len(self.lines)
        start = end-number
        result = ""

        if start<0:
            start = 0

        for index in range(start,end):
            line = self.lines[index]
            if line[0]:
                result += "<- "
            else:
                result += "-> "
            result += line[1]
            result += "\n"

        return result

    def hasChanges(self):
        result = self.changes
        self.changes = False
        return result
