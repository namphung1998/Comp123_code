from tkinter import *
class CanvasExperiment:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 400, height = 400)
        self.canvas.grid(row = 0, column = 0)

        self.circ = self.canvas.create_oval(100,100,300,300, fill = "yellow")
        self.eye1 = self.canvas.create_oval(150,150,180,180, fill = "black")
        self.eye2 = self.canvas.create_oval(220,150,250,180 , fill = "black")
        self.mouth = self.canvas.create_arc(150,150,250,250, style = CHORD, fill = "black", start = 225,extent = 90)



    def go(self):
        self.root.mainloop()

ce = CanvasExperiment()
ce.go()