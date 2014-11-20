"""Project PSIT"""
from Tkinter import *

class Application(Frame):
    def createWidgets(self):
        L1 = Label(self, text="Insert Password")
        L1.grid(row=0, column=0)
        E1 = Entry(self, bd=5)
        E1.focus_set()
        E1.grid(row=0, column=1)
        B1 = Button(self, text="OK")
        B1.grid(row=0, column=2)
        B1["command"] = self.printresult
        
    def printresult(self):
        print "Your Password is normally secret"
        
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.geometry("450x450")
root.title("Secret Enough? | The PSIT Project")
app = Application(master=root)
app.mainloop()

