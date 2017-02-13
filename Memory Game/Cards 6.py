from tkinter import *
import random
import time




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


       titleLabel = Label(self.root, text="Memory Game", font=("Abble Chancery", 50), fg="Black")
       titleLabel.grid(row=0, column=0)


       authorLabel = Label(self.root, text="By Elena Youngdale and Nam Phung")
       authorLabel.grid(row=3, column=0)


       self.startbtn = Button(self.root, text="START",
                              command=self.openandcover)  ###command = start pop up a new window
       self.startbtn.grid(row=2, column=0)


       self.lstclick=[] #is used to check for sucessful pairs of 2
       self.sucesspairs=[] #is used to see if the game is done or not. once len=16, game is over


       self.lst = []
       self.lstofpositions = []
       self.pairpos = []
       self.coverPositions = []
       self.numClick = 0

   def createPairs(self, color, shape):
       if shape == "square":
           for i in range(2):
               curr_pos = random.choice(self.positions)
               self.canvas.create_rectangle(curr_pos, fill=color)
               self.positions.remove(curr_pos)
               self.pairpos.append(curr_pos)
           self.lstofpositions.append(self.pairpos)
           self.pairpos = []


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

       self.rs = self.createPairs("red", "square")
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
       self.Coverup()


   def openandcover(self):
       self.openwind()
       self.root.after(5000, self.coverImages)


   def Coverup(self):
       self.canvas.tag_bind(self.lst[0], "<Button-1>", lambda x: self.dell0())
       self.canvas.tag_bind(self.lst[1], "<Button-1>", lambda x: self.dell1())
       self.canvas.tag_bind(self.lst[2], "<Button-1>", lambda x: self.dell2())
       self.canvas.tag_bind(self.lst[3], "<Button-1>", lambda x: self.dell3())
       self.canvas.tag_bind(self.lst[4], "<Button-1>", lambda x: self.dell4())
       self.canvas.tag_bind(self.lst[5], "<Button-1>", lambda x: self.dell5())
       self.canvas.tag_bind(self.lst[6], "<Button-1>", lambda x: self.dell6())
       self.canvas.tag_bind(self.lst[7], "<Button-1>", lambda x: self.dell7())
       self.canvas.tag_bind(self.lst[8], "<Button-1>", lambda x: self.dell8())
       self.canvas.tag_bind(self.lst[9], "<Button-1>", lambda x: self.dell9())
       self.canvas.tag_bind(self.lst[10], "<Button-1>", lambda x: self.dell10())
       self.canvas.tag_bind(self.lst[11], "<Button-1>", lambda x: self.dell11())
       self.canvas.tag_bind(self.lst[12], "<Button-1>", lambda x: self.dell12())
       self.canvas.tag_bind(self.lst[13], "<Button-1>", lambda x: self.dell13())
       self.canvas.tag_bind(self.lst[14], "<Button-1>", lambda x: self.dell14())
       self.canvas.tag_bind(self.lst[15], "<Button-1>", lambda x: self.dell15())


   def dell0(self):
       self.lstclick.append(self.lst[0])
       self.sucesspairs.append(self.lst[0])
       self.canvas.delete(self.lst[0])
       self.coverPositions.append(self.positions2[0])
       self.numClick = self.numClick + 1
       self.doClick()


   def dell1(self):
       self.lstclick.append(self.lst[1])
       self.sucesspairs.append(self.lst[1])
       self.canvas.delete(self.lst[1])
       self.coverPositions.append(self.positions2[1])
       self.numClick = self.numClick + 1
       self.doClick()


   def dell2(self):
       self.lstclick.append(self.lst[2])
       self.sucesspairs.append(self.lst[2])
       self.canvas.delete(self.lst[2])
       self.coverPositions.append(self.positions2[2])
       self.numClick = self.numClick + 1
       self.doClick()

   def dell3(self):
       self.lstclick.append(self.lst[3])
       self.sucesspairs.append(self.lst[3])
       self.canvas.delete(self.lst[3])
       self.coverPositions.append(self.positions2[3])
       self.numClick = self.numClick + 1
       self.doClick()


   def dell4(self):
       self.lstclick.append(self.lst[4])
       self.sucesspairs.append(self.lst[4])
       self.canvas.delete(self.lst[4])
       self.coverPositions.append(self.positions2[4])
       self.numClick = self.numClick + 1
       self.doClick()


   def dell5(self):
       self.lstclick.append(self.lst[5])
       self.sucesspairs.append(self.lst[5])
       self.canvas.delete(self.lst[5])
       self.coverPositions.append(self.positions2[5])
       self.doClick()


   def dell6(self):
       self.lstclick.append(self.lst[6])
       self.sucesspairs.append(self.lst[6])
       self.canvas.delete(self.lst[6])
       self.coverPositions.append(self.positions2[6])
       self.doClick()

   def dell7(self):
       self.lstclick.append(self.lst[7])
       self.sucesspairs.append(self.lst[7])
       self.canvas.delete(self.lst[7])
       self.coverPositions.append(self.positions2[7])
       self.numClick = self.numClick + 1
       self.doClick()

   def dell8(self):
       self.lstclick.append(self.lst[8])
       self.sucesspairs.append(self.lst[8])
       self.canvas.delete(self.lst[8])
       self.coverPositions.append(self.positions2[8])
       self.numClick = self.numClick + 1
       self.doClick()

   def dell9(self):
       self.lstclick.append(self.lst[9])
       self.sucesspairs.append(self.lst[9])
       self.canvas.delete(self.lst[9])
       self.coverPositions.append(self.positions2[9])
       self.numClick = self.numClick + 1
       self.doClick()


   def dell10(self):
       self.lstclick.append(self.lst[10])
       self.sucesspairs.append(self.lst[10])
       self.canvas.delete(self.lst[10])
       self.coverPositions.append(self.positions2[10])
       self.numClick = self.numClick + 1
       self.doClick()

   def dell11(self):
       self.lstclick.append(self.lst[11])
       self.sucesspairs.append(self.lst[11])
       self.canvas.delete(self.lst[11])
       self.coverPositions.append(self.positions2[11])
       self.numClick = self.numClick + 1
       self.doClick()

   def dell12(self):
       self.lstclick.append(self.lst[12])
       self.sucesspairs.append(self.lst[12])
       self.canvas.delete(self.lst[12])
       self.coverPositions.append(self.positions2[12])
       self.numClick = self.numClick + 1
       self.doClick()


   def dell13(self):
       self.lstclick.append(self.lst[13])
       self.sucesspairs.append(self.lst[13])
       self.canvas.delete(self.lst[13])
       self.coverPositions.append(self.positions2[13])
       self.numClick = self.numClick + 1
       self.doClick()

   def dell14(self):
       self.lstclick.append(self.lst[14])
       self.sucesspairs.append(self.lst[14])
       self.canvas.delete(self.lst[14])
       self.coverPositions.append(self.positions2[14])
       self.numClick = self.numClick + 1
       self.doClick()

   def dell15(self):
       self.lstclick.append(self.lst[15])
       self.sucesspairs.append(self.lst[15])
       self.canvas.delete(self.lst[15])
       self.coverPositions.append(self.positions2[15])
       self.numClick = self.numClick + 1
       self.doClick()

   def disableall(self):
       for button in self.cover:
           self.button(state=DISABLED)

   def enableall(self):
       for button in self.allbuttons:
           self.button(state=NORMAL)

   def doClick(self):
       if self.numClick == 2:
            if self.coverPositions in self.pairpos:
                pass
            else:
                for pos in self.coverPositions:
                    cover = self.canvas.create_rectangle(pos, fill="black")
                    self.lst.append(cover)
       else:
           pass
       self.coverPositions = []
       self.numclick = 0
   def go(self):
       self.root.mainloop()
       print(self.lstofpositions)




win = Window()


win.go()




















