from Tkinter import *
from math import *

class Welcome():
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x100')
        self.master.title('Secret Enough?')

        self.label1 = Label(self.master, text='Welcome to the Secret Enough? Application')
        self.label1.grid(row=0, column=2)
        self.lable2 = Label(self.master, text='Which funtion you want to use?')
        self.lable2.grid(row=1, column=2)
        self.button1 = Button(self.master, text='Identify Password', fg='blue', command=self.gotoCalPass)
        self.button1.grid(row=4, column=1, columnspan=1)
        self.button2 = Button(self.master, text='Generate Password', fg='blue', command=self.gotoGePass)
        self.button2.grid(row=4, column=2, columnspan=1)
        self.button3 = Button(self.master, text='Exit', fg='red', command=self.finish)
        self.button3.grid(row=4, column=3, columnspan=1)



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
        self.force = IntVar()
        self.master = master
        self.master.geometry('600x300')
        self.master.title('Password Identify')

        self.label = Label(self.master, text='This is a Password Identify Page')
        self.label.grid(row=0, column=0)
        self.label2 = Label(self.master, text='Please insert password that you want to identify')
        self.label2.grid(row=1, column=0)
        self.passtext = Entry(self.master, textvariable=self.text)
        self.passtext.grid(row=1, column=2)
        self.label3 = Label(self.master, text='Please insert speed of guessing')
        self.label3.grid(row=2, column=0, sticky='W')
        self.passforce = Entry(self.master, textvariable=self.force)
        self.passforce.grid(row=2, column=2)
        self.force.set(1000)
        self.label4 = Label(self.master, text='guessing/sec')
        self.label4.grid(row=2, column=3)
        self.button = Button(self.master, text='OK', fg='blue', command=self.checkpass)
        self.button.grid(row=3, column=1)
        self.button = Button(self.master, text='Back', fg='red', command=self.back)
        self.button.grid(row=3, column=0)


    def checkpass(self):
        upper, lower, number, symbol = 0, 0, 0, 0
        passtext = self.text.get()
        force = self.force.get()
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
        probanum = self.probaCrackPass(textlist, force, passtext)
        self.labelresult = Label(self.master, text='Your password have :')
        self.labelresult.grid_forget()
        self.labelresult.grid(row=4, column=0, sticky='W')
        self.labelupper = Label(self.master, text='%d  Upper case' % upper)
        self.labelupper.grid_forget()
        self.labelupper.grid(row=4, column=1)
        self.labellower = Label(self.master, text='%d  Lower case' % lower)
        self.labellower.grid_forget()
        self.labellower.grid(row=4, column=2)
        self.labelnumber = Label(self.master, text='%d  Digit' % number)
        self.labelnumber.grid_forget()
        self.labelnumber.grid(row=4, column=3)
        self.labelsymbol = Label(self.master, text='%d  Symbol' % symbol)
        self.labelsymbol.grid_forget()
        self.labelsymbol.grid(row=4, column=4)
        self.labeltextproba = Label(self.master, text='Your password has '+str(probanum[0])+' possible case')
        self.labeltextproba.grid_forget()
        self.labeltextproba.grid(row=5, column=0, sticky='W')
        self.labelcrack = Label(self.master, text='Your password has will cracked in')
        self.labelcrack.grid_forget()
        self.labelcrack.grid(row=6, column=0, sticky='W')
        count = 0
        col = 7
        lst_prefix = ['years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds']
        check = all(letter == 0 for letter in probanum[1])
        if check == False:
            for ele in probanum[1]:
                self.labeldata = Label(self.master, text=str(ele) +' '+ lst_prefix[count])
                if self.labeldata.winfo_exists():
                    self.labeldata.grid_forget()
                self.labeldata.grid(row=col, column=0)
                col += 1
                count += 1
        else:
            self.labeldata = Label(self.master, text='Your password will cracked in no time!')
            if self.labeldata.winfo_exists():
                    self.labeldata.grid_forget()
            self.labeldata.grid(row=7, column=0)
        
    def probaCrackPass(self, textlist, force, data):
        probanum = factorial(len(data)) / factorial(len(data) - len(data))
        #Calculate time that use to crack password aka bruteforce
        crack = []
        check = all(letter == data[0] for letter in data)
        if check == False:
            seconds = int(probanum / force) #time second
            crack.append(seconds)
            minutes, seconds = divmod(seconds, 60)
            crack.append(minutes)
            hours, minutes = divmod(minutes, 60)
            crack.append(hours)
            days, hours = divmod(hours, 24)
            crack.append(days)
            weeks, days = divmod(days, 7)
            crack.append(weeks)
            months, weeks = divmod(weeks, 4)
            crack.append(months)
            years, months = divmod(months, 12)
            crack.append(years)
        else:
            crack = [0]
            attemp = 1
            probanum = 1
        return probanum, crack
                                        
    def back(self):
        self.master.destroy()

class GenePass():
    def __init__(self, master):
        self.upper = IntVar()
        self.lower = IntVar()
        self.digit = IntVar()
        self.symbol = IntVar()
        self.master = master
        self.master.geometry('500x200')
        self.master.title('Password Genereter')

        self.label = Label(self.master, text='This is a Password Gereneter Page')
        self.label.grid(row=0, column=0)
        self.labellen = Label(self.master, text='How length for the password')
        self.labellen.grid(row=1, column=0)
        self.passlen = Spinbox(self.master, from_=4, to=20, state=NORMAL)
        self.passlen.grid(row=1, column=1)
        self.button = Button(self.master, text='OK', fg='blue', command=self.genPass)
        self.button.grid(row=1, column=2)
##        self.labelUpper = Label(self.master, text='Upper Case')
##        self.labelUpper.grid(row=2, column=0)
        self.checkUpper = Checkbutton(self.master, text='Upper Case', variable=self.upper)
        self.checkUpper.grid(row=3, column=0)
##        self.labelLower = Label(self.master, text='Lower Case')
##        self.labelLower.grid(row=2, column=1)
        self.checkLower = Checkbutton(self.master, text='Lower Case', variable=self.lower)
        self.checkLower.grid(row=3, column=1)
##        self.labelDigit = Label(self.master, text='Digit')
##        self.labelDigit.grid(row=2, column=2)
        self.checkDigit = Checkbutton(self.master, text='Digit', variable=self.digit)
        self.checkDigit.grid(row=3, column=2)
##        self.labelSymbol = Label(self.master, text='Symbol')
##        self.labelSymbol.grid(row=2, column=3)
        self.checkSymbol = Checkbutton(self.master, text='Symbol', variable=self.symbol)
        self.checkSymbol.grid(row=3, column=3)

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
