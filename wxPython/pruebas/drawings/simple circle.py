import wx


class Ventana(wx.Frame):

    """Draw a line to a panel."""

    def __init__(self, padre=None, id=-1, pos=wx.DefaultPosition, title="Draw on Panel"):
        self.size = (1000, 1000)
        wx.Frame.__init__(self, padre, id, title, pos, size) # Inicializa la clase padre de la ventana, que es wx.Frame
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, 4))
        dc.DrawLine(0, 0, 50, 50)

class Aplicacion(wx.App):
    """La clase Aplicacion hereda de la clase padre wx.App y sirve para crear una aplicacion"""
    def OnInit(self):
        """Inicializa la clase Aplicacion"""
        self.ventana1 = Ventana() # Crea una instancia de clase Ventana
        self.ventana1.Show() # Muestra la ventana
        self.SetTopWindow(self.ventana1) # Asigna ventana1 como la ventana principal de la app
        return True

if __name__ == '__main__':
    miAplic = Aplicacion() # Crea una instancia de la clase MiAplic
    miAplic.MainLoop() # Llama al metodo MainLoop para comenzar a capturar eventos de teclado y raton, evitando asi que se cierre la aplicacion nada mas abrirse
