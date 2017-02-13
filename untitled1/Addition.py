from tkinter import *

class Addition:
    def __init__(self):


        self.root = Tk()
        aLabel = Label(self.root, text="A")
        aLabel.grid(row=0,column=0)

        bLabel = Label(self.root, text="B")
        bLabel.grid(row=1,column=0)

        abLabel = Label(self.root, text="A+B")
        abLabel.grid(row=2, column=0)

        abLabel2 = Label(self.root, text="A-B")
        abLabel2.grid(row=3, column=0)

        self.resultLabel = Label(self.root, text=0)
        self.resultLabel.grid(row=2,column=1)

        self.subLabel = Label(self.root, text = 0)
        self.subLabel.grid(row=3,column=1)



        self.aEntry = Entry(self.root)
        self.aEntry.grid(row=0,column=1)

        self.bEntry = Entry(self.root)
        self.bEntry.grid(row=1, column=1)

        subButton = Button(self.root, text="Subtract", command =self.doSubtraction)
        subButton.grid(row = 2,column=2)

        goButton = Button(self.root, text="GO!", command=self.doAddition)
        goButton.grid(row=0,column=2)

        quitButton = Button(self.root, text="QUIT!", command = self.quit)
        quitButton.grid(row=1, column=2)

    def doAddition(self):
        aVal = self.aEntry.get()
        aVal = int(aVal)
        bVal = self.bEntry.get()
        bVal = int(bVal)
        abVal = aVal+bVal
        self.resultLabel.config(text=abVal)

    def doSubtraction(self):
        aVal = int(self.aEntry.get())
        bVal = int(self.bEntry.get())
        sub = aVal - bVal
        self.subLabel.config(text=sub)


    def go(self):
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

window = Addition()
window.go()