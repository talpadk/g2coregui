import wx


class GCodeTextRenderPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.onSize)
        self.Bind(wx.EVT_PAINT, self.onPaint)
    def onSize(self, event):
        event.Skip()
        self.Refresh()
        
    def onPaint(self, event):
        w, h = self.GetClientSize()
        dc = wx.AutoBufferedPaintDC(self)
        dc.SetBackground(wx.Brush(wx.Colour(255,255,255), style=wx.BRUSHSTYLE_SOLID))
        dc.Clear()
        dc.DrawLine(0, 0, w, h)

        
#        self.SetBackgroundStyle(wx.BG_STYLE_PAINT);
#        self.canvas = wx.AutoBufferedPaintDC(self)

class GCodeTextViewer(wx.Panel):
    def __init__(self, parent, wxId):
        wx.Panel.__init__(self, parent, wxId)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.render = GCodeTextRenderPanel(self)
        self.scrollBar = wx.ScrollBar(parent=self, style=wx.SB_VERTICAL)


        
        self.sizer.Add(self.render, 1, wx.RIGHT|wx.EXPAND, 3)
        self.sizer.Add(self.scrollBar, 0, wx.EXPAND, 0)

        self.SetSizerAndFit(self.sizer)
