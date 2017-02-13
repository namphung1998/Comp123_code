from tkinter import *

class ButtonGUI:
    def __init__(self):
        self.rootWin = Tk()
        self.rootWin.title("Button and Label GUI")

        quitButton = Button(self.rootWin, text="QUIT", command = self.quit)
        quitButton.grid(row=0,column=0)

        helloButton = Button(self.rootWin, text="HELLO", command = self.hello)
        helloButton.grid(row=1, column = 0)

        byeButton = Button(self.rootWin, text="GOODBYE", command = self.bye)
        byeButton.grid(row=2, column = 0)

        lab1 = Label(self.rootWin,text = "Welcome.")
        lab1.grid(row = 1, column = 1)

        self.sv = StringVar()
        lab =  Label(self.rootWin,textvariable = self.sv)
        lab.grid(row = 1, column = 2)
        self.sv.set("Welcome.")


    def quit(self):
        self.rootWin.destroy()

    def hello(self):
        self.sv.set("Hello")

    def bye(self):
        self.sv.set("Goodbye")

    def go(self):
        self.rootWin.mainloop()

myG = ButtonGUI()
myG.go()

###Part 2 Pig Latin GUI
class PigLatin:
    def __init__(self):
        self.win = Tk()
        self.win.title("Pig Latin GUI")

        self.userText = StringVar()

        aLabel = Label(self.root, text="A")
        aLabel.grid(row=0, column=0)

        bLabel = Label(self.root, text="B")
        bLabel.grid(row=1, column=0)

        entry = Entry(self.win, textvariable = self.userText)

