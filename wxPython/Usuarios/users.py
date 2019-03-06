"""Aplicacion de gestión de usuarios"""

class LoginGUI(wx.Frame):
    def __init__(self, registro, parent=None, id=-1, title="Juego tres en raya: login"):
        wx.Frame.__init__(self, parent, id, title)
        self.SetBackgroundColour(wx.WHITE)
        self.registro = registro
        # Preparamos la barra de menu
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menu1.Append(101, "&Salir", "Haz clic para salir")
        menuBar.Append(menu1, "&TresEnRaya")
        self.SetMenuBar(menuBar)
        wx.EVT_MENU(self, 101, self.OnSalir)
        nombreUsuarioLabel = wx.StaticText(self, -1, "Nombre usuario:")
        self.nombreUsuarioTxtCtrl= wx.TextCtrl(self, -1, "", size=(125, -1))
        passwordLabel = wx.StaticText(self, -1, "Password:")
        self.passwordTxtCtrl = wx.TextCtrl(self, -1, "", size=(125, -1),
        style=wx.TE_PASSWORD)

        self.botonNuevoUsuario = wx.Button(self, -1, "Nuevo usuario")
        wx.EVT_BUTTON(self, self.botonNuevoUsuario.GetId(), self.OnNuevoUsuario)
        self.botonLogin = wx.Button(self, -1, "Login")
        self.botonLogin.Enable(False)
        wx.EVT_BUTTON(self, self.botonLogin.GetId(), self.OnLogin)
        self.botonSalir = wx.Button(self, -1, "Salir")
        wx.EVT_BUTTON(self, self.botonSalir.GetId(), self.OnSalir)
        bsizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        topSizer.Add(nombreUsuarioLabel, 0, wx.GROW|wx.ALL, 4)
        topSizer.Add(self.nombreUsuarioTxtCtrl, 0, wx.GROW|wx.ALL|wx.ALIGN_RIGHT , 4)
        bsizer.Add(topSizer, 0, wx.GROW|wx.ALL, 4)

        botonAccionSizer = wx.BoxSizer(wx.HORIZONTAL)
        botonAccionSizer.Add(self.botonNuevoUsuario, 0, wx.GROW|wx.ALL, 4)

        bsizer.Add(botonAccionSizer, 0, wx.GROW|wx.ALL, 4)
        bsizer.Fit(self)
        self.SetAutoLayout(True)
        self.SetSizer(bsizer)
        wx.EVT_CLOSE(self, self.OnSalir)



import wx

if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub


########################################################################
class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Login")

        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label="Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.ALL, 5)

        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        p_sizer.Add(self.password, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        btn = wx.Button(self, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(main_sizer)

    #----------------------------------------------------------------------
    def onLogin(self, event):
        """
        Check credentials and login
        """
        stupid_password = "pa$$w0rd!"
        user_password = self.password.GetValue()
        if user_password == stupid_password:
            print "You are now logged in!"
            pub.sendMessage("frameListener", message="show")
            self.Destroy()
        else:
            print "Username or password is incorrect!"

########################################################################
class MyPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)


########################################################################
class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Main App")
        panel = MyPanel(self)
        pub.subscribe(self.myListener, "frameListener")

        # Ask user to login
        dlg = LoginDialog()
        dlg.ShowModal()

    #----------------------------------------------------------------------
    def myListener(self, message, arg2=None):
        """
        Show the frame
        """
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

import wx

########################################################################
class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Login")
        self.logged_in = False

        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)

        user_lbl = wx.StaticText(self, label="Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.user = wx.TextCtrl(self)
        user_sizer.Add(self.user, 0, wx.ALL, 5)

        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)
        p_sizer.Add(self.password, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        btn = wx.Button(self, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(main_sizer)

    #----------------------------------------------------------------------
    def onLogin(self, event):
        """
        Check credentials and login
        """
        stupid_password = "pa$$w0rd!"
        user_password = self.password.GetValue()
        if user_password == stupid_password:
            print "You are now logged in!"
            self.logged_in = True
            self.Close()
        else:
            print "Username or password is incorrect!"

########################################################################
class MyPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)


########################################################################
class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Main App")
        panel = MyPanel(self)

        # Ask user to login
        dlg = LoginDialog()
        dlg.ShowModal()
        authenticated = dlg.logged_in
        if not authenticated:
            self.Close()

        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
