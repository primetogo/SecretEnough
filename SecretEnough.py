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
        self.text = StringVar()
        self.master = master
        self.master.geometry('600x200')
        self.master.title('Password Identify')

        self.label = Label(self.master, text='This is a Password Identify Page')
        self.label.grid(row=0, column=0)
        self.label2 = Label(self.master, text='Please insert password that you want to identify')
        self.label2.grid(row=1, column=0)
        self.passtext = Entry(self.master, textvariable=self.text)
        self.passtext.grid(row=1, column=2)
        self.button = Button(self.master, text='OK', fg='blue', command=self.checkpass)
        self.button.grid(row=1, column=3)

        self.button = Button(self.master, text='Back', fg='red', command=self.back)
        self.button.grid(row=7, column=0)


    def checkpass(self):
        upper, lower, number, symbol = 0, 0, 0, 0
        passtext = self.text.get()
        for text in passtext:
            if text.isupper():
                upper += 1
            elif text.islower():
                lower += 1
            elif text.isdigit():
                number += 1
            else:
                symbol += 1
        textlist = [upper, lower, number, symbol]
        probanum = self.probaCrackPass(textlist)
        self.labelresult = Label(self.master, text='Your password have :')
        self.labelresult.grid(row=2, column=0)
        self.labelupper = Label(self.master, text='%d Upper case' % upper)
        self.labelupper.grid(row=3, column=0)
        self.labellower = Label(self.master, text='%d Lower case' % lower)
        self.labellower.grid(row=3, column=1)
        self.labelnumber = Label(self.master, text='%d Digit' % number)
        self.labelnumber.grid(row=3, column=2)
        self.labelsymbol = Label(self.master, text='%d Symbol' % symbol)
        self.labelsymbol.grid(row=3, column=3)
        self.labelproba = Label(self.master, text='Probability to crack is : %.15f ' % probanum + ' %')
        self.labelproba.grid(row=5, column=0)

        
        
    def probaCrackPass(self, textlist):
        #print textlist
        probanum = 0
        upper = 26 ** textlist[0]  
        lower = 26 ** textlist[1]  
        number = 10 ** textlist[2]
        symbol = 38 ** textlist[3]
        probanum = upper * lower * number * symbol
        probanum = 1.0 / (probanum / 100.0)
        #print probanum
        return probanum
                                 
            


    def back(self):
        self.master.destroy()

class GenePass():
    def __init__(self, master):
        #self.lentext = IntVar()
        self.master = master
        self.master.geometry('500x200')
        self.master.title('Password Genereter')

        self.label = Label(self.master, text='This is a Password Gereneter Page')
        self.label.grid(row=0, column=0)
        self.labellen = Label(self.master, text='How length for the password')
        self.labellen.grid(row=1, column=0)
        self.passlen = Spinbox(self.master, from_=1, to=20, state=NORMAL)
        self.passlen.grid(row=1, column=1)
        self.button = Button(self.master, text='OK', fg='blue', command=self.genPass)
        self.button.grid(row=1, column=2)

        self.button = Button(self.master, text='Back', fg='red', command=self.back)
        self.button.grid(row=9, column=0)


    def genPass(self):
        lenpass = self.passlen.get()
        print lenpass

    def back(self):
        self.master.destroy()


def main():
    root = Tk()
    myGUIWelcome = Welcome(root)
    root.mainloop()

if __name__ == '__main__':
    main()
