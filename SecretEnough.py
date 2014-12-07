from Tkinter import *

class Welcome():
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x200')
        self.master.title('Secret Enough?')

        self.label1 = Label(self.master, text='Welcome to the Secret Enough? Application')
        self.label1.grid(row=0, column=1)
        self.lable2 = Label(self.master, text='Which funtion you want to use?')
        self.lable2.grid(row=1, column=1)
        self.button1 = Button(self.master, text='Identify Password', fg='blue', command=self.gotoCalPass)
        self.button1.grid(row=6, column=0)
        self.button2 = Button(self.master, text='Generate Password', fg='blue', command=self.gotoGePass)
        self.button2.grid(row=6, column=1)
        self.button3 = Button(self.master, text='Exit', fg='red', command=self.finish)
        self.button3.grid(row=6, column=2)



    def gotoCalPass(self):
        root2 = Toplevel(self.master)
        myGUI = IdenPass(root2)


    def gotoGePass(self):
        root3 = Toplevel(self.master)
        myGUI = GenePass(root3)
    


    def finish(self):
        self.master.destroy()
        


class IdenPass():
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x200')
        self.master.title('Password Identify')

        self.button = Button(self.master, text='Back', fg='red', command=self.back)
        self.button.grid(row=0, column=0)
        


    def back(self):
        self.master.destroy()

class GenePass():
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x200')
        self.master.title('Password Genereter')

        self.button = Button(self.master, text='Back', fg='red', command=self.back)
        self.button.grid(row=0, column=0)

    def back(self):
        self.master.destroy()


def main():
    root = Tk()
    myGUIWelcome = Welcome(root)
    root.mainloop()

if __name__ == '__main__':
    main()
