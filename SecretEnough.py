from Tkinter import *
import tkFont
from math import *

################################################################################

class Welcome():
    def __init__(self, master):
        self.master = master
        self.master.geometry('640x150')
        self.master.title('Secret Enough?')
        quark_b = tkFont.Font(family= "Quark", size= 18, weight="bold")
        quark_l = tkFont.Font(family= "Quark", size= 16, weight="bold")
        quark_button = tkFont.Font(family= "Quark", size= 13, weight="bold")
        self.label1 = Label(self.master, text='Welcome to the Secret Enough? Application', font=quark_b)
        self.label1.grid(row=0, column=2)
        self.lable2 = Label(self.master, text='Which funtion you want to use?', font=quark_l)
        self.lable2.grid(row=1, column=2)
        self.button1 = Button(self.master, text='Identify Password', fg='blue', font=quark_button, command=self.gotoCalPass)
        self.button1.grid(row=4, column=1, columnspan=1)
        self.button2 = Button(self.master, text='Generate Password', fg='blue', font=quark_button, command=self.gotoGePass)
        self.button2.grid(row=4, column=2, columnspan=1)
        self.button3 = Button(self.master, text='Exit', fg='red', font=quark_button, command=self.finish)
        self.button3.grid(row=4, column=3, columnspan=1)



    def gotoCalPass(self):
        root2 = Toplevel(self.master)
        myGUI = IdenPass(root2)


    def gotoGePass(self):
        root3 = Toplevel(self.master)
        myGUI = GenePass(root3)
    


    def finish(self):
        self.master.destroy()
        
################################################################################

class IdenPass():
    def __init__(self, master):
        #Initialization identified password windows
        self.text = StringVar()
        self.force = IntVar()
        self.master = master
        self.master.geometry('850x460')
        self.master.title('Password Identify')
        quark_b = tkFont.Font(family= "Quark", size= 18, weight="bold")
        quark_l = tkFont.Font(family= "Quark", size= 13, weight="bold")
        quark_button = tkFont.Font(family= "Quark", size= 13, weight="bold")
        self.label = Label(self.master, text= \
                      'This is a Password Identify Page', font=quark_l)
        self.label.grid(row=0, column=0)
        self.label2 = Label(self.master, text= \
                        'Please insert password that you want to identify', \
                        font=quark_l)
        self.label2.grid(row=1, column=0)
        self.passtext = Entry(self.master, textvariable=self.text, font=quark_l)
        self.passtext.grid(row=1, column=2)
        self.label3 = Label(self.master, text='Please insert speed of finding', font=quark_l)
        self.label3.grid(row=2, column=0, sticky='W')
        self.passforce = Entry(self.master, textvariable=self.force, font=quark_l)
        self.passforce.grid(row=2, column=2)
        self.force.set(1000)
        self.label4 = Label(self.master, text='combination/sec', font=quark_l)
        self.label4.grid(row=2, column=3)
        self.button = Button(self.master, text='OK', fg='blue', \
                       command=self.checkpass, font=quark_button)
        self.button.grid(row=3, column=1)
        self.button = Button(self.master, text='Back', fg='red', \
                        command=self.back, font=quark_button)
        self.button.grid(row=3, column=0)
                        

    def countstring(self, text):
        upper, lower, number, symbol = 0, 0, 0, 0
        color = ['red', 'red', 'red', 'red']
        for letter in text:
            if letter.isupper():
                upper += 1
            elif letter.islower():
                lower += 1
            elif letter.isdigit():
                number += 1
            else:
                symbol += 1
        if upper > 0:
            color[0] = 'green'
        if lower > 0:
            color[1] = 'green'
        if number > 0:
            color[2] = 'green'
        if symbol > 0:
            color[3] = 'green'
        return upper, lower, number, symbol, color
    
    def checkpass(self):
        quark_l = tkFont.Font(family= "Quark", size= 13, weight="bold")
        passtext = self.text.get()
        force = self.force.get()
        textlist = self.countstring(passtext)
        probanum = self.probaCrackPass(textlist, force, passtext)
        self.labelresult = Label(self.master, text='Your password have :', \
                            font=quark_l)
        self.labelresult.grid_forget()
        self.labelresult.grid(row=4, column=0)
        self.labelupper = Label(self.master, text='%d  Upper case' % \
                            textlist[0], font=quark_l, fg=textlist[4][0])
        self.labelupper.grid_forget()
        self.labelupper.grid(row=4, column=1, stick='W')
        self.labellower = Label(self.master, text='%d  Lower case' % \
                            textlist[1], font=quark_l, fg=textlist[4][1])
        self.labellower.grid_forget()
        self.labellower.grid(row=4, column=2)
        self.labelnumber = Label(self.master, text='%d  Digit' % \
                               textlist[2], font=quark_l, fg=textlist[4][2])
        self.labelnumber.grid_forget()
        self.labelnumber.grid(row=4, column=3)
        self.labelsymbol = Label(self.master, text='%d  Symbol' % \
                               textlist[3], font=quark_l, fg=textlist[4][3])
        self.labelsymbol.grid_forget()
        self.labelsymbol.grid(row=4, column=4)
        self.labeltextproba = Label(self.master, text=\
                                 'Your password has ' + str(probanum[0]) + \
                                 ' combination till cracked', font=quark_l)
        self.labeltextproba.grid_forget()
        self.labeltextproba.grid(row=5, column=0, sticky='W')
        self.labelcrack = Label(self.master, text= \
                            'Your password has will cracked in', font=quark_l)
        self.labelcrack.grid_forget()
        self.labelcrack.grid(row=6, column=0, sticky='W')
        count = 0
        col = 7
        lst_prefix = ['years', 'months', 'weeks',
                       'days', 'hours', 'minutes', 'seconds']
        for ele in probanum[1]:
            self.labeldata = Label(self.master, text=str(ele) +' '+ \
                                lst_prefix[count], font=quark_l)
            self.labeldata.grid_forget()
            self.labeldata.grid(row=col, column=0)
            col += 1
            count += 1
        
    def probaCrackPass(self, textlist, force, data):
        probanum = textlist[0] ** len(data) + textlist[1] ** len(data) + \
                   textlist[2] ** len(data) + textlist[3] ** len(data)
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

################################################################################

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
