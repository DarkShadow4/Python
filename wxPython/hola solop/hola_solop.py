import wx

class Ventana(wx.Frame):
    """Clase frame que visualiza una ventana."""
    def __init__(self, imagen, padre=None, id=-1, pos=wx.DefaultPosition, titulo="Hola solo programadores"):
        """Crea una instancia de Frame y visualiza una imagen."""
        temp = imagen.ConvertToBitmap() # Convierte la imagen a bitmap
        size = temp.GetWidth(), temp.GetHeight() # Obtiene el tamaño de la imagen
        wx.Frame.__init__(self, padre, id, titulo, pos, size) # Inicializa la clase padre de la ventana, que es wx.Frame
        self.bmp = wx.StaticBitmap(self, -1, temp) # Inicializa el atributo self.bmp con una instancia de un control wx.StaticBitmap que contiene el bitmap creado antes

class MiAplic(wx.App):
    """La clase aplicacion."""
    def OnInit(self):
        wx.InitAllImageHandlers() # Inicializa los gestores de imagenes
        imagen = wx.Image("solop.jpg", wx.BITMAP_TYPE_JPEG) # Crea una instancia de imagen pasando como parametros el nombre de la imagen y el tipo/formato
        self.miVentana = Ventana(imagen) # Crea una instancia de la clase ventana pasando la imagen para que la pueda mostrar
        self.miVentana.Show() # Muestra la ventana
        self.SetTopWindow(self.miVentana) # Asigna la ventana como la ventana principal de la app
        return True

if __name__ == "__main__":
    miAplic = MiAplic() # Crea una instancia de la clase MiAplic
    miAplic.MainLoop() # Llama al metodo MainLoop para comenzar a capturar eventos de teclado y raton, evitando asi que se cierre la aplicacion nada mas abrirse
