from tkinter import *
from Cards4 import *


class StartWind:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=600)


        titleLabel = Label(self.root, text="Memory Game",font=("Abble Chancery",100),fg="Black")
        titleLabel.grid(row=0, column=0)


        authorLabel = Label(self.root,text="By Elena Youngdale and Nam Phung")
        authorLabel.grid(row=2,column=0)


        startbtn = Button(self.root,text = "START",command=self.openwind) ###command = start pop up a new window
        startbtn.grid(row=1, column=0)


    def openwind(self):
        self.canvas.grid(row=0,column=0)

        self.createPairs("red", "square")
        self.createPairs("green", "square")
        self.createPairs("blue", "square")
        self.createPairs("yellow", "square")
        self.createPairs("red", "circle")
        self.createPairs("green", "circle")
        self.createPairs("blue", "circle")
        self.createPairs("yellow", "circle")

    def go(self):
        self.root.mainloop()

win = StartWind()
win.go()