import wx

class Ventana(wx.Frame):
    """Clase Ventana que hereda de la clase padre wx.Frame para visualizar una ventana."""
    def __init__(self, padre=None, id=-1, pos=wx.DefaultPosition, titulo="App de un circulo dibujado"):
        size = 1000, 1000
        wx.Frame.__init__(self, padre, id, titulo, pos, size) # Inicializa la clase padre de la ventana, que es wx.Frame

    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, 4))
        dc.DrawCircle(500, 500, 500)

class MiAplic(wx.App):
    """La clase MiAplic hereda de la clase padre wx.App y sirve para crear una aplicacion"""
    def OnInit(self):
        """Inicializa la clase MiAplic"""
        self.ventana1 = Ventana() # Crea una instancia de clase Ventana
        self.ventana1.Show() # Muestra la ventana
        self.SetTopWindow(self.ventana1) # Asigna ventana1 como la ventana principal de la app
        return True

if __name__ == "__main__":
    miAplic = MiAplic() # Crea una instancia de la clase MiAplic
    miAplic.MainLoop() # Llama al metodo MainLoop para comenzar a capturar eventos de teclado y raton, evitando asi que se cierre la aplicacion nada mas abrirse
