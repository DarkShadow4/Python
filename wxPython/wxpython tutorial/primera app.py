# -*- coding: utf-8 -*-

import wx

class Ventana(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent=parent, title=title)

        self.Colors = wx.ColourDatabase()

        self.sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.text_box = wx.TextCtrl(self, style = wx.TE_MULTILINE) # Input miltilinea de texto
        self.button_1 = wx.Button(self, -1, u"Botón 1", size = (150, -1)) # Boton (se pone una u antes de las comillas para indicar que es un texto unicode)
        self.button_2 = wx.Button(self, -1, u"Botón 2", size = (150, -1)) # Boton (se pone una u antes de las comillas para indicar que es un texto unicode)

        # sizer.Add(control, proporcion, flag, borde) el flag es como el estilo
        self.sizer1.Add(self.text_box, 2, wx.EXPAND | wx.ALL, 10)
        self.sizer1.Add(self.button_1, 1, wx.ALIGN_CENTER | wx.ALL, 10)
        self.sizer1.Add(self.button_2, 1, wx.ALIGN_CENTER | wx.ALL, 10)

        #Sizer
        self.SetSizer(self.sizer1)

        #Evento
        self.Bind(wx.EVT_BUTTON, self.onClick)# Event handler Bind(Tipo_evento, handler, source)

        self.SetSize((300, 200))
        self.Centre(True)
        self.Show()

    def onClick(self, event):
        self.etiqueta = event.GetEventObject().GetLabel()
        print self.etiqueta

if __name__ == "__main__":
    app = wx.App()
    ventana1 = Ventana(None, u"Título random")
    app.MainLoop()
