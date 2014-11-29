"""How was your password?"""
from Tkinter import *

class Application(Frame):
    def createWidgets(self):
        label_input = Label(self, text="Insert Password")
        label_input.grid(row=0, column=0)
        pass_input = Entry(self, bd=5)
        pass_input.focus_set()
        pass_input.grid(row=0, column=1)
        btn_check = Button(self, text="OK")
        btn_check.grid(row=0, column=2)
        btn_check["command"] = self.basic_data(pass_input)
        #cannot operate need to pass password input
        #from pass_input to basic data

    def basic_data(self, password): #calculate inside password
        upper = 0
        lower = 0
        symbols = 0
        number = 0
        get_pass = password.get()
        for element in get_pass:
            if element.isalpha():
                if element.isupper():
                    upper += 1
                else:
                    lower += 1
            elif element.isdigit():
                number += 1
            else:
                symbols += 1
        if upper == 0:
            upper = "No upper case"
        elif lower == 0:
            lower = "No lower case"
        elif symbols == 0:
            symbols = "No symbols"
        elif number == 0:
            number = "No number"
        label_upper = Label(self, text=str(upper))
        label_upper.grid(row=0)
        label_lower = Label(self, text=str(lower))
        label_lower.grid(row=0)
        label_symbols = Label(self, text=str(symbols))
        label_symbols.grid(row=0)
        label_number = Label(self, text=str(number))
        label_number.grid(row=0)
             
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        

root = Tk()
root.geometry("450x450")
root.title("Secret Enough? | The PSIT Project")

app = Application(master=root)
app.mainloop()

