from tkinter import *

# In this question you will complete a tkinter interface.
# This interface is designed to help students understand
# how the pyhton and works. The logical and operation is
# true if and only if both of the values are true, so x
# and y is true only if x and y are true. The interface
# has two buttons allow the user to toggle the value of x
# and y from true to false. Currently only the widgets
# have been placed. Your job is to complete this interface
# so that the buttons will toggle the values of x and y,
# and, if both x and y are true the value of x and y
# should be shown as true as well. To make this problem
# easier the widget code is all provided, you may, however,
# want to modify it to add commands and/or stringvariables
# to allow you to complete your job. Note: this interface
# uses many labels to help instruct the user, most
# of these labels should be ignored.

class AndGateSimulator:
    def __init__(self):
        self.root = Tk()

        self.xButton = Button(self.root, text="switch X", command = self.changeX)
        self.xButton.grid(row=0, column=0)

        self.yButton = Button(self.root, text="switch Y", command = self.changeY)
        self.yButton.grid(row=2, column=0)

        # you may want to switch this label from a text
        # to use a textvariable
        self.xVal = StringVar()
        self.xLab = Label(self.root, textvariable = self.xVal)
        self.xLab.grid(row=0, column=2)
        self.xVal.set("False")

        # decorative label
        self.xDecLab = Label(self.root, text="X = ")
        self.xDecLab.grid(row=0, column=1)

        # you may want to switch this label from a text
        # to use a textvariable\
        self.yVal = StringVar()
        self.yLab = Label(self.root, textvariable = self.yVal)
        self.yLab.grid(row=2, column=2)
        self.yVal.set("False")
        #decorative label
        self.yDecLab = Label(self.root, text="Y =")
        self.yDecLab.grid(row=2, column=1)

        # Decorative label (this doesn't need to change)
        self.decLab = Label(self.root, text="X and Y =")
        self.decLab.grid(row=1, column=3)

        # Output Label
        # you may want to switch this label from a text
        # to use a textvariable
        self.out = StringVar()
        self.outLab = Label(self.root, textvariable = self.out)
        self.outLab.grid(row=1, column=4)
        self.out.set("False")


    def changeX(self):
        self.xVal.set("True")
        self.xVal.set("False")
        self.checkTrue()


    def changeY(self):
        self.yVal.set("False")

        self.yVal.set("True")
        self.checkTrue()

    def checkTrue(self):
        if self.xVal == "True" and self.yVal == "True":
            self.out.set("True")
        else:
            self.out.set("False")

    def go(self):
        self.root.mainloop()

interface = AndGateSimulator()
interface.go()