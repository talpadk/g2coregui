#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import gettext
import g2coreGuiLayout
import g2coreProtocol
import g2coreGuiBackend

class G2coreGui(wx.App):
    def OnInit(self):
        mainFrame = g2coreGuiLayout.MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(mainFrame)
        mainFrame.Show()
        self.backend = g2coreGuiBackend.g2coreGuiBackend(self)
        self.protocol = g2coreProtocol.g2coreProtocol() #should be done as a UI event
        self.backend.setProtocol(self.protocol)
        self.timer = myTimer(self.backend)
        self.backend.appendUserCommandToQueue('G1 X10 F100')
        return True

class myTimer(wx.Timer):
    def __init__(self, backend):
        wx.Timer.__init__(self)
        self.backend = backend

    def Notify(self):
        self.backend.animate()

    
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = G2coreGui(0)
    app.timer.Start(100)
    app.MainLoop()    
