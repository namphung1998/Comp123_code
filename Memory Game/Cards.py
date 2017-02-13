from tkinter import *
import random


class Window():
    def __init__(self):
        shapes = {1: "square", 2: "circle"}
        colors = {1: "red", 2: "green", 3: "blue"}
        positions = {1:(40,40,125,125), 2:(185,40,270,125), 3:(330,40,415,125), 4:(475,40,560,125),
                     5:(40,185,125,270), 6:(185,185,270,270), 7:(330,185,415,270), 8:(475,185,560,270),
                     9:(40,330,125,415), 10:(185,330,270,415), 11:(330,330,415,415), 12:(475,330,560,415),
                     13:(40,475,125,560), 14:(185,475,270,560), 15:(330,475,415,560), 16:(475,475,560,560)}


        self.root = Tk()
        self.canvas = Canvas(self.root, width = 600, height = 600)
        self.canvas.grid(row = 0, column = 0)

        for i in range(8):
            s = random.randint(1,3)
            if s == 1:
                self.card = self.canvas.create_rectangle((positions.get(random.randrange(1,17))),fill = (colors.get((random.randrange(1,4)))))

            elif s == 2:
                self.card = self.canvas.create_arc((positions.get(random.randrange(1,17))), fill =(colors.get((random.randrange(1,4)))), start = 225,extent = 90)
            elif s == 3:
                self.card = self.canvas.create_oval((positions.get(random.randrange(1,17))),fill = (colors.get((random.randrange(1,4)))))


    def go(self):
        self.root.mainloop()




win = Window()
win.go()


win = Window()
win.go()


