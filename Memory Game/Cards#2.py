from tkinter import *
import random

class Window():
    def __init__(self):
        shapes = {1: "square", 2: "circle"}
        colors = {1: "red", 2: "green", 3: "blue", 4:"yellow"}
        positions = {1:(40,40,125,125), 2:(185,40,270,125), 3:(330,40,415,125), 4:(475,40,560,125),
                     5:(40,185,125,270), 6:(185,185,270,270), 7:(330,185,415,270), 8:(475,185,560,270),
                     9:(40,330,125,415), 10:(185,330,270,415), 11:(330,330,415,415), 12:(475,330,560,415),
                     13:(40,475,125,560), 14:(185,475,270,560), 15:(330,475,415,560), 16:(475,475,560,560)}
        countSquare = 0
        countCircle = 0


        self.root = Tk()
        self.canvas = Canvas(self.root, width = 600, height = 600)
        self.canvas.grid(row = 0, column = 0)



        for i in range(8):
            s = random.randrange(1,3-x)
            if s == 1:
                countSquare = countSquare + 2
            else:
                countCircle = countSquare + 2

            for a in range(2):
                p = random.randrange(1,17-a)
                self.card = self.canvas.create_rectangle((positions.get(p)),fill = (colors.get((random.randrange(1,4)))))
                del positions[p]

            if count








    def go(self):
        self.root.mainloop()




win = Window()
win.go()


win = Window()
win.go()


