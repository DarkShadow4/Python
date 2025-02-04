#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4.1 on Thu Mar 30 11:13:24 2006

import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.button_1 = wx.Button(self, wx.ID_OK, "")
        self.__set_properties()
        self.__do_layout()
        self.Bind(wx.EVT_BUTTON, self.OnBtn1, self.button_1)
     # end wxGlade
    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("event-glade")
        self.SetSize((350, 250))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.button_1, 0, wx.ADJUST_MINSIZE, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def OnBtn1(self, event): # wxGlade: MyFrame.<event_handler>
        self.button_1.SetLabel("Ouch!")
        event.Skip()

    # end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MyFrame(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

    # end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
