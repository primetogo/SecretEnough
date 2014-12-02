"""How was your password?"""
from Tkinter import *

class Application(Frame):
    def createWidgets(self):
        label_input = Label(self, text="Insert Password")
        label_input.grid(row=1, column=0)
        pass_input = Entry(self, bd=5)
        pass_input.focus_set()
        pass_input.grid(row=1, column=1)
        btn_check = Button(self, text="Check it")
        btn_check.grid(row=1, column=2)
        btn_check["command"] = self.display(pass_input)
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
        if lower == 0:
            lower = "No lower case"
        if symbols == 0:
            symbols = "No symbols"
        if number == 0:
            number = "No number"
        packed = [upper, lower, symbols, number]
        return packed
    
    def display(self, password):
            data_in = self.basic_data(password)
            label_upper = Label(self, text=str(data_in[0]))
            label_upper.grid(row=2, column=1)
            label_lower = Label(self, text=str(data_in[1]))
            label_lower.grid(row=3, column=1)
            label_symbols = Label(self, text=str(data_in[2]))
            label_symbols.grid(row=4, column=1)
            label_number = Label(self, text=str(data_in[3]))
            label_number.grid(row=5, column=1)

    
                  
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        

root = Tk()
root.geometry("450x450")
root.title("Secret Enough?")

app = Application(master=root)
app.mainloop()

