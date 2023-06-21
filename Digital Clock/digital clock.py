from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title("Digital Clock")
root.resizable(False,False)
def none():
    text = strftime(' %H:%M:%S %p ')
    Label1.config(text = text)
    Label1.after(1000,none)
Label1 = Label(root,font=('digital-7' ,50,'bold'), background='black',foreground='lightblue')
Label1.pack(anchor='center')
none()


root.mainloop()