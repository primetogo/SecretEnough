'''
Project PSIT - SecretEnough?
Do it by :
Apisit Seekaewnit 55070138
Panupong Prueksa 55070089
'''
from Tkinter import *
from math import *
import tkMessageBox
import tkFont
import random
from num2words import num2words


################################################################################

class Welcome():
    '''Class Welcome'''
    def __init__(self, master):
        '''Install the constructor of widgets'''
        self.master = master
        self.master.geometry('640x150')
        self.master.title('Secret Enough?')
        quark_b = tkFont.Font(family= "Quark", size= 18, weight="bold")
        quark_l = tkFont.Font(family= "Quark", size= 16, weight="bold")
        quark_button = tkFont.Font(family= "Quark", size= 13, weight="bold")
        self.label1 = Label(self.master, text= \
                         'Welcome to the Secret Enough? Application', font=quark_b)
        self.label1.grid(row=0, column=2)
        self.lable2 = Label(self.master, text='Which function you want to use?',\
                         font=quark_l)
        self.lable2.grid(row=1, column=2)
        self.button1 = Button(self.master, text='Identify Password', fg='blue', \
                           font=quark_button, command=self.gotoCalPass)
        self.button1.grid(row=4, column=1, columnspan=1)
        self.button2 = Button(self.master, text='Generate Password', fg='blue', \
                           font=quark_button, command=self.gotoGePass)
        self.button2.grid(row=4, column=2, columnspan=1)
        self.button3 = Button(self.master, text='Exit', fg='red', \
                           font=quark_button, command=self.finish)
        self.button3.grid(row=4, column=3, columnspan=1)



    def gotoCalPass(self):
        '''Go to Identify Password Page'''
        root2 = Toplevel(self.master)
        myGUI = IdenPass(root2)


    def gotoGePass(self):
        '''Go to Genereter Password Page'''
        root3 = Toplevel(self.master)
        myGUI = GenePass(root3)
    


    def finish(self):
        '''Close the program'''
        self.master.destroy()
        
################################################################################

class IdenPass():
    '''Class Identify Password'''
    def __init__(self, master):
        '''Install the constructor of widgets'''
        self.text = StringVar()
        self.force = IntVar()
        self.master = master
        self.master.geometry('850x460')
        self.master.title('Password Identify')
        quark_b = tkFont.Font(family= "Quark", size= 16, weight="bold")
        quark_l = tkFont.Font(family= "Quark", size= 13, weight="bold")
        quark_button = tkFont.Font(family= "Quark", size= 13, weight="bold")
        self.label = Label(self.master, text= \
                      'This is a Password Identify Page', font=quark_b)
        self.label.grid(row=0, column=1)
        self.label2 = Label(self.master, text= \
                        'Please insert password for identify', \
                        font=quark_l)
        self.label2.grid(row=1, column=0)
        self.passtext = Entry(self.master, textvariable=self.text, font=quark_l)
        self.passtext.grid(row=1, column=1)
        self.label3 = Label(self.master, text='Please insert speed of finding', font=quark_l)
        self.label3.grid(row=2, column=0, sticky='W')
        self.passforce = Spinbox(self.master, from_=1000, to=9000000, state=NORMAL, font=quark_l)
        self.passforce.grid(row=2, column=1)
        self.label4 = Label(self.master, text='combination/sec', font=quark_l)
        self.label4.grid(row=2, column=3)
        self.button = Button(self.master, text='OK', fg='blue', \
                       command=self.checkpass, font=quark_button)
        self.button.grid(row=3, column=1)
        self.button = Button(self.master, text='Back', fg='red', \
                        command=self.back, font=quark_button)
        self.button.grid(row=1, column=3)
                        

    def countstring(self, text):
        '''Find the element of Password'''
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
            color[0] = 'blue'
        if lower > 0:
            color[1] = 'blue'
        if number > 0:
            color[2] = 'blue'
        if symbol > 0:
            color[3] = 'blue'
        return upper, lower, number, symbol, color
    
    def checkpass(self):
        '''Identify Password'''
        upper, color_up = StringVar(), StringVar()
        lower, color_down = StringVar(), StringVar()
        digit, color_digit = StringVar(), StringVar()
        symbol, color_sym = StringVar(), StringVar()
        comb_num = StringVar()
        year, month, week, day, hour, minute, second = StringVar(), \
        StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), \
        StringVar()
        quark_l = tkFont.Font(family= "Quark", size= 13, weight="bold")
        passtext = self.text.get()
        force = self.passforce.get()
        textlist = self.countstring(passtext)
        probanum = self.probaCrackPass(textlist, force, passtext)
        upper.set(str(textlist[0]) + ' Upper Case  ')
        color_up.set(textlist[4][0])
        lower.set(str(textlist[1]) + ' Lower case  ')
        color_down.set(textlist[4][1])
        digit.set(str(textlist[2]) + ' Digit  ')
        color_digit.set(textlist[4][2])
        symbol.set(str(textlist[3]) + ' Symbol  ')
        color_sym.set(textlist[4][3])
        comb_num.set("Your password has " + str(probanum[0]) + " combination " + \
                          "it cracked!")
        year.set(probanum[1][0])
        month.set(probanum[1][1])
        week.set(probanum[1][2])
        day.set(probanum[1][3])
        hour.set(probanum[1][4])
        minute.set(probanum[1][5])
        second.set(probanum[1][6])
    
        self.labelresult = Label(self.master, text='Your password contains :', \
                            font=quark_l)
        self.labelresult.grid(row=4, column=0)
        self.labelupper = Label(self.master, text=upper.get(), \
                            font=quark_l, fg=color_up.get())
        self.labelupper.grid(row=5, column=0)
        self.labellower = Label(self.master, text=lower.get(), \
                            font=quark_l, fg=color_down.get())
        self.labellower.grid(row=6, column=0)
        self.labelnumber = Label(self.master, text=digit.get(), \
                               font=quark_l, fg=color_digit.get())
        self.labelnumber.grid(row=7, column=0)
        self.labelsymbol = Label(self.master, text=symbol.get(), \
                               font=quark_l, fg=color_sym.get())
        self.labelsymbol.grid(row=8, column=0)
        self.labeltextproba = Label(self.master, text=comb_num.get(), font=quark_l)
        self.labeltextproba.grid(row=4, column=1)
        self.labelcrack = Label(self.master, text= \
                            'Your password has will cracked in', font=quark_l)
        self.labelcrack.grid(row=5, column=1)
        self.labelyear = Label(self.master, text=year.get()+ " -->  " + \
                             num2words(int(year.get())) + " Years", font=quark_l)
        self.labelyear.grid(row=6, column=1)
        self.labelmonth = Label(self.master, text=month.get() + " -->  " + \
                             num2words(int(month.get())) + " Months", font=quark_l)
        self.labelmonth.grid(row=7, column=1)
        self.labelweek = Label(self.master, text=week.get() + " -->  " + \
                             num2words(int(week.get())) + " Weeks", font=quark_l)
        self.labelweek.grid(row=8, column=1)
        self.labelday = Label(self.master, text=day.get() + " -->  " + \
                             num2words(int(day.get())) + " Days", font=quark_l)
        self.labelday.grid(row=9, column=1)
        self.labelhour = Label(self.master, text=hour.get() + " -->  " + \
                             num2words(int(hour.get())) + " Hours", font=quark_l)
        self.labelhour.grid(row=10, column=1)
        self.labelminute = Label(self.master, text=minute.get() + " -->  " + \
                                num2words(int(minute.get())) + " Minutes", font=quark_l)
        self.labelminute.grid(row=11, column=1)
        self.labelsecond = Label(self.master, text=second.get() + " -->  " + \
                             num2words(int(second.get())) + " Seconds", font=quark_l)
        self.labelsecond.grid(row=12, column=1)
        
        
        
    def probaCrackPass(self, textlist, force, data):
        '''Find the time to crack password'''
        probanum = textlist[0] ** len(data) + textlist[1] ** len(data) + \
                   textlist[2] ** len(data) + textlist[3] ** len(data)
        #Calculate time that use to crack password aka bruteforce
        #use combination number / speed
        crack = []
        seconds = int(probanum / int(force)) 
        crack.append(seconds)                       #record time in seconds
        minutes, seconds = divmod(seconds, 60)
        crack.append(minutes)                       #record time in minutes
        hours, minutes = divmod(minutes, 60)
        crack.append(hours)                          #record time in hours
        days, hours = divmod(hours, 24)
        crack.append(days)                           #record time in days
        weeks, days = divmod(days, 7)
        crack.append(weeks)                         #record time in weeks
        months, weeks = divmod(weeks, 4)
        crack.append(months)                       #record time in months
        years, months = divmod(months, 12)
        crack.append(years)                         #record time in years
        return probanum, crack
                                        
    def back(self):
        '''Close the Page'''
        self.master.destroy()

################################################################################

class GenePass():
    '''Class Genereter Password'''
    def __init__(self, master):
        '''Install the constructor of widgets'''
        self.upper = IntVar()
        self.lower = IntVar()
        self.digit = IntVar()
        self.symbol = IntVar()
        self.master = master
        self.master.geometry('650x200')
        self.master.title('Password Genereter')
        quark_b = tkFont.Font(family= "Quark", size= 16, weight="bold")
        quark_l = tkFont.Font(family= "Quark", size= 13, weight="bold")
        self.label = Label(self.master, text='This is a Password Gereneter Page', font=quark_b)
        self.label.grid(row=0, column=1)
        self.labellen = Label(self.master, text='How length for the password', font=quark_l)
        self.labellen.grid(row=1, column=0)
        self.passlen = Spinbox(self.master, from_=4, to=20, state=NORMAL, font=quark_l)
        self.passlen.grid(row=1, column=1)
        self.button = Button(self.master, text='OK', fg='blue', command=self.checkoption, font=quark_l)
        self.button.grid(row=1, column=2)
        self.checkUpper = Checkbutton(self.master, text='Upper Case', variable=self.upper, font=quark_l)
        self.checkUpper.grid(row=3, column=0)
        self.checkLower = Checkbutton(self.master, text='Lower Case', variable=self.lower, font=quark_l)
        self.checkLower.grid(row=3, column=1)
        self.checkDigit = Checkbutton(self.master, text='Digit', variable=self.digit, font=quark_l)
        self.checkDigit.grid(row=3, column=2)
        self.checkSymbol = Checkbutton(self.master, text='Symbol', variable=self.symbol, font=quark_l)
        self.checkSymbol.grid(row=3, column=3)
        self.button = Button(self.master, text='Back', fg='red', command=self.back, font=quark_l)
        self.button.grid(row=9, column=0)
        
    def checkoption(self):
        '''Check the checkbox before generate password'''
        isupper = self.upper.get()
        islower = self.lower.get()
        isdigit = self.digit.get()
        issymbol = self.symbol.get()
        check = int(isupper) + int(islower) + int(isdigit) + int(issymbol)
        if check == 0:
            tkMessageBox.showinfo('Error', 'Please check at least one checkbox')
        else:
            self.genPass(isupper, islower, isdigit, issymbol)


    def genPass(self, isupper, islower, isdigit, issymbol):
        '''Generate Password'''
        strpass = ''
        lenpass = self.passlen.get()
        
        listsymbol = [33, 35, 36, 37, 38, 63, 64]
        lenpass = int(lenpass)
        
        while len(strpass) < lenpass:
            if isupper:
                strpass += self.randomchar([65, 90])
                if len(strpass) == lenpass:
                    break
            if islower:
                strpass += self.randomchar([97, 122])
                if len(strpass) == lenpass:
                    break
            if isdigit:
                strpass += self.randomchar([48, 57])
                if len(strpass) == lenpass:
                    break
            if issymbol:
                temp = self.randomsymbol(listsymbol)
                strpass += temp
                if len(strpass) == lenpass:
                    break
        strpass = self.shufflePass(strpass)
        self.showpass(strpass)
    def showpass(self, strpass):
        '''Show password from genereter'''
        quark_l = tkFont.Font(family= "Quark", size= 13, weight="bold")
        self.text = StringVar()
        self.labelpass = Label(self.master, text='Here is a password :', font=quark_l)
        self.labelpass.grid(row=4, column=0)
        self.text.set(strpass)
        self.showtext = Entry(self.master, textvariable=self.text, font=quark_l)
        self.showtext.grid(row=4, column=1)

    def randomchar(self, numrange):
        '''Random upper case, lower case and digit'''
        return chr(random.randint(numrange[0], numrange[1]))

    def randomsymbol(self, listsymbol):
        '''Random symbol'''
        return chr(listsymbol[random.randint(0, len(listsymbol)-1)])

    def shufflePass(self, strpass):
        '''Shuffle Password after fihish generate'''
        return ''.join(random.sample(strpass, len(strpass)))
        
        

    def back(self):
        '''Close genereter password Page'''
        self.master.destroy()


def main():
    '''Start the Program'''
    root = Tk()
    myGUIWelcome = Welcome(root)
    root.mainloop()

if __name__ == '__main__':
    main()
