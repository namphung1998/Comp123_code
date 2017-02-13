from tkinter import *
import random

class Window():
    def __init__(self):
        self.positions = [(40, 40, 125, 125), (185, 40, 270, 125), (330, 40, 415, 125), (475, 40, 560, 125),
                          (40, 185, 125, 270), (185, 185, 270, 270), (330, 185, 415, 270), (475, 185, 560, 270),
                          (40, 330, 125, 415), (185, 330, 270, 415), (330, 330, 415, 415), (475, 330, 560, 415),
                          (40, 475, 125, 560), (185, 475, 270, 560), (330, 475, 415, 560), (475, 475, 560, 560)]
        self.positions2 = [(40, 40, 125, 125), (185, 40, 270, 125), (330, 40, 415, 125), (475, 40, 560, 125),
                           (40, 185, 125, 270), (185, 185, 270, 270), (330, 185, 415, 270), (475, 185, 560, 270),
                           (40, 330, 125, 415), (185, 330, 270, 415), (330, 330, 415, 415), (475, 330, 560, 415),
                           (40, 475, 125, 560), (185, 475, 270, 560), (330, 475, 415, 560), (475, 475, 560, 560)]


        self.root = Tk()


        titleLabel = Label(self.root, text="Memory Game", font=("Abble Chancery", 80), fg="Black")
        titleLabel.grid(row=0, column=0)


        authorLabel = Label(self.root, text="By Elena Youngdale and Nam Phung")
        authorLabel.grid(row=3, column=0)


        self.startbtn = Button(self.root, text="START",
                               command=self.openandcover)  ###command = start pop up a new window
        self.startbtn.grid(row=2, column=0)


        self.lst = []
        self.lstofpositions = []
        self.pairpos = []


    def createPairs(self, color, shape):
        if shape == "square":
            for i in range(2):
                curr_pos = random.choice(self.positions)
                self.canvas.create_rectangle(curr_pos, fill=color)
                self.positions.remove(curr_pos)
                self.pairpos.append(curr_pos)
            self.lstofpositions.append(self.pairpos)
            self.pairpos=[]

        elif shape == "circle":
            for i in range(2):
                curr_pos = random.choice(self.positions)
                self.canvas.create_oval(curr_pos, fill=color)
                self.positions.remove(curr_pos)
                self.pairpos.append(curr_pos)
            self.lstofpositions.append(self.pairpos)
            self.pairpos = []

    def openwind(self):
        self.canvas = Canvas(self.root, width=600, height=600)
        self.canvas.grid(row=1, column=0)
        self.startbtn.grid_forget()

        self.createPairs("red", "square")
        self.createPairs("green", "square")
        self.createPairs("blue", "square")
        self.createPairs("yellow", "square")
        self.createPairs("red", "circle")
        self.createPairs("green", "circle")
        self.createPairs("blue", "circle")
        self.createPairs("yellow", "circle")

    def coverImages(self):
        for p in range(16):
            position = self.positions2[p]
            cover = self.canvas.create_rectangle(position, fill="black")
            self.lst.append(cover)

        self.canvas.tag_bind(self.lst[0], "<Button-1>", lambda x: self.canvas.delete(self.lst[0]))
        self.canvas.tag_bind(self.lst[1], "<Button-1>", lambda x: self.canvas.delete(self.lst[1]))
        self.canvas.tag_bind(self.lst[2], "<Button-1>", lambda x: self.canvas.delete(self.lst[2]))
        self.canvas.tag_bind(self.lst[3], "<Button-1>", lambda x: self.canvas.delete(self.lst[3]))
        self.canvas.tag_bind(self.lst[4], "<Button-1>", lambda x: self.canvas.delete(self.lst[4]))
        self.canvas.tag_bind(self.lst[5], "<Button-1>", lambda x: self.canvas.delete(self.lst[5]))
        self.canvas.tag_bind(self.lst[6], "<Button-1>", lambda x: self.canvas.delete(self.lst[6]))
        self.canvas.tag_bind(self.lst[7], "<Button-1>", lambda x: self.canvas.delete(self.lst[7]))
        self.canvas.tag_bind(self.lst[8], "<Button-1>", lambda x: self.canvas.delete(self.lst[8]))
        self.canvas.tag_bind(self.lst[9], "<Button-1>", lambda x: self.canvas.delete(self.lst[9]))
        self.canvas.tag_bind(self.lst[10], "<Button-1>", lambda x: self.canvas.delete(self.lst[10]))
        self.canvas.tag_bind(self.lst[11], "<Button-1>", lambda x: self.canvas.delete(self.lst[11]))
        self.canvas.tag_bind(self.lst[12], "<Button-1>", lambda x: self.canvas.delete(self.lst[12]))
        self.canvas.tag_bind(self.lst[13], "<Button-1>", lambda x: self.canvas.delete(self.lst[13]))
        self.canvas.tag_bind(self.lst[14], "<Button-1>", lambda x: self.canvas.delete(self.lst[14]))
        self.canvas.tag_bind(self.lst[15], "<Button-1>", lambda x: self.canvas.delete(self.lst[15]))


    def openandcover(self):
        self.openwind()
        self.root.after(4000, self.coverImages)

    def click0(self):
        self.canvas.delete(self.lst[0])

    def go(self):
        self.root.mainloop()
        print(self.lstofpositions)







win = Window()
win.go()




















