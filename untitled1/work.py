from tkinter import *

class Yeller:
    def __init__(self):
        self.root = Tk()

        self.inptVar = StringVar()

        self.inpt = Entry(self.root, font = ("Bradley Hand", 30), textvariable = self.inptVar)
        self.inpt.grid(row = 0, column = 0)

        self.btn = Button(self.root, text = "yell now!", command = self.click)
        self.btn.grid(row=0, column=1)

        self.outVar = StringVar()
        self.outVar.set("HEY THERE YALL")

        self.out = Label(self.root, font = ("Bradley Hand",30), textvariable = self.outVar)
        self.out.grid(row=1, column = 0, columnspan = 2)

    def go(self):
        self.root.mainloop()

    def click(self):
        inStr = self.inptVar.get()
        capsStr = inStr.upper()
        self.outVar.set(capsStr)

yell = Yeller()
yell.go()
