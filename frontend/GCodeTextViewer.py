import wx


class GCodeTextRenderPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        self.gCodeFile = None #The g-code file we are rendering
        self.offset = 0       #The current viewing offset
        self.drawingEnabled = False #Signals drawing okay, a workaround for a gtk late window creation issue

        self.numberOfVisibleLines = None
        
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.onSize)
        self.Bind(wx.EVT_PAINT, self.onPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.onWindowCreate)
        
    def setGCodeFile(self, gCodeFile):
        self.gCodeFile = gCodeFile
        self.offset = 0
        self.drawText()
        
    def onSize(self, event):
        event.Skip()
        self.Refresh()

    def onWindowCreate(self, event):
        self.drawingEnabled = True
        self.drawText()
        
    def onPaint(self, event):
        self.drawText()

    def setScrollOffset(self, offset):
        oldOffset = self.offset
        self.offset = offset
        if self.offset != oldOffset:
            self.drawText()
        
    def drawText(self):
        if (not self.drawingEnabled):
            return
        w, h = self.GetClientSize()
        dc = wx.AutoBufferedPaintDC(self)
        dc.SetBackground(wx.Brush(wx.Colour(255,255,255), style=wx.BRUSHSTYLE_SOLID))
        dc.Clear()

        lineHeight = dc.GetCharHeight();
        dcSize = dc.GetSize();

        self.numberOfVisibleLines = dcSize.GetHeight()/lineHeight
        
        yPosition = 0
        if self.gCodeFile != None:
            for i in range(self.numberOfVisibleLines+1):
                text = self.gCodeFile.getLineN(i+self.offset)
                if text != None:
                    dc.DrawText(text,0,yPosition)
                    yPosition = yPosition+lineHeight
        self.parent.calculateScrollBarSize()            
        

class GCodeTextViewer(wx.Panel):
    def __init__(self, parent, wxId):
        wx.Panel.__init__(self, parent, wxId)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.render = GCodeTextRenderPanel(self)
        self.scrollBar = wx.ScrollBar(parent=self, style=wx.SB_VERTICAL)
        
        self.sizer.Add(self.render, 1, wx.RIGHT|wx.EXPAND, 3)
        self.sizer.Add(self.scrollBar, 0, wx.EXPAND, 0)

        self.SetSizerAndFit(self.sizer)

        self.scrollBar.Bind(wx.EVT_SCROLL, self.onScroll)


        
    def setGCodeFile(self, gCodeFile):
        self.render.setGCodeFile(gCodeFile)
        self.calculateScrollBarSize()
        
    def calculateScrollBarSize(self):
        numberOfLinesInFile = 1
        if self.render.gCodeFile != None:
            numberOfLinesInFile = self.render.gCodeFile.getNumberOfLines()
        numberOfVisibleLines = self.render.numberOfVisibleLines
        position = self.scrollBar.GetThumbPosition()
        if numberOfVisibleLines == None:
            self.scrollBar.SetScrollbar(position, 16, numberOfLinesInFile, 15)
        else:
            maxValue = numberOfLinesInFile
            if maxValue < 0:
                maxValue = 0
            scrollStepSize = numberOfVisibleLines-1
            if scrollStepSize<1:
                scrollStepSize = 1
            if numberOfVisibleLines<1:
                numberOfVisibleLines = 1
            self.scrollBar.SetScrollbar(position, numberOfVisibleLines, maxValue, scrollStepSize)

            
    def onScroll(self, event):
        self.render.setScrollOffset(self.scrollBar.GetThumbPosition())

