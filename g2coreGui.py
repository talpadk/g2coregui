#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
scriptPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(scriptPath+"/backend")

import wx
import gettext
import g2coreGuiLayout
import g2coreProtocol
import g2coreGuiBackend

class G2coreGui(wx.App):
    def OnInit(self):
        self.mainFrame = g2coreGuiLayout.MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.mainFrame)
        self.mainFrame.Show()
        self.backend = g2coreGuiBackend.g2coreGuiBackend(self)
        self.protocol = g2coreProtocol.g2coreProtocol() #should be done as a UI event
        self.backend.setProtocol(self.protocol)
        self.timer = myTimer(self.backend)
        return True

class myTimer(wx.Timer):
    def __init__(self, backend):
        wx.Timer.__init__(self)
        self.backend = backend

    def Notify(self):
        self.backend.animate()
        application = wx.App.Get()
        if self.backend.logHistory.hasChanges():
            application.mainFrame.updateLog(self.backend.logHistory)
        if self.backend.digitalReadOut.hasChanges():
            application.mainFrame.updateDRO(self.backend.digitalReadOut)
    
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = G2coreGui(0)
    app.timer.Start(100)
    app.MainLoop()    
