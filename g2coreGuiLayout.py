#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.2 on Wed Jul 26 10:28:47 2017
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.terminal = wx.Panel(self, wx.ID_ANY)
        self.log = wx.TextCtrl(self.terminal, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.manualInput = wx.TextCtrl(self.terminal, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.onManualInput, self.manualInput)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle(_("g2coreGUI"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        terminalSizer = wx.BoxSizer(wx.VERTICAL)
        terminalSizer.Add(self.log, 1, wx.ALL | wx.EXPAND, 3)
        terminalSizer.Add(self.manualInput, 0, wx.ALL | wx.EXPAND, 3)
        self.terminal.SetSizer(terminalSizer)
        sizer_1.Add(self.terminal, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def onManualInput(self, event):  # wxGlade: MainFrame.<event_handler>
        application = wx.App.Get()
        application.backend.appendUserCommandToQueue(self.manualInput.GetValue())
        self.manualInput.Clear()

    def updateLog(self, logHistory):
        self.log.SetValue(logHistory.getLastNLinesAsText(100))
        self.log.SetInsertionPointEnd()
        
# end of class MainFrame
