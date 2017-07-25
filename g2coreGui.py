#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import gettext
import g2coreGuiLayout
import g2coreGuiBackend



class G2coreGui(wx.App):
    def OnInit(self):
        mainFrame = g2coreGuiLayout.MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(mainFrame)
        mainFrame.Show()
        return True

class myTimer(wx.Timer):
    def __init__(self):
        wx.Timer.__init__(self)
        self.Start(10)

    def Notify(self):
        global backend
        backend.animate()

    
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = G2coreGui(0)
    timer = myTimer()
    app.MainLoop()    
