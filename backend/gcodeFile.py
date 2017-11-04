class gcodeFile:

    
    def __init__(self, filename):
        self.lines = []
        self.position = 0
        self.numberOfLines = 0
        with open(filename, 'r') as fileHandle:
            for line in fileHandle:
                line = line.strip()
                self.lines.append(line)
                self.numberOfLines += 1;

    def getLine(self):
        if self.position<self.numberOfLines:
            result = self.lines[self.position]
            self.position += 1
            return result
        else:
            return None

    def getLineN(self, n):
        if n<self.numberOfLines:
            return self.lines[n]
        else:
            return None;

    def getNumberOfLines(self):
        return self.numberOfLines
        
    def hasMoreData(self):
        if self.position<self.numberOfLines:
            return True
        else:
            return False
