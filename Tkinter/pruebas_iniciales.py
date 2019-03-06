from Tkinter import *

class Application(Frame):
    """A class representing the window program"""
    def say_hi(self):
        """Prints an output"""
        print "hi there, everyone!"

    def createWidgets(self):
        """A method that creates the widgets"""
        self.QUIT = Button(self) # Defines and initialices QUIT as a Button
        self.QUIT["text"] = "QUIT" # Gives the hi_there button a text
        self.QUIT["fg"]   = "red" # Gives the hi_there button a color
        self.QUIT["command"] =  self.quit # Assigns a command to the hi_there button; in this case it closes the window and ends the program

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self) # Defines and initialices hi_there as a Button
        self.hi_there["text"] = "Hello", # Gives the hi_there button a text
        self.hi_there["command"] = self.say_hi # Assigns a command to the hi_there button; in this case it calls the say_hi method

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
