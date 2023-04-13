# This is a sample Python script.
from tkinter import *
class Myfullname:
    def __init__(self, Name):
        self.lbl1 = Label(win, text="MY GIVEN NAME")  # for label widget
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(win, text="MY MIDDLE NAME.")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(win, text="LAST NAME")
        self.lbl3.place(x=100, y=150)
        self.lbl4 = Label(win, text="MY FULL NAME")
        self.lbl4.place(x=150, y=200)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=200, y=50)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=100)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=200, y=150)
        self.txt4 = Entry(win, bd=4)
        self.txt4.place(x=200, y=200)
        self.btnFull = Button(name,text = "MY Full Name")

    def given(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def middle(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def full(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))

    def clr(self):
        self.txt1.delete(0, "end")
        self.txt2.delete(0, "end")
        self.txt3.delete(0, "end")

window = Tk()
Myfull = myfullname (window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()















