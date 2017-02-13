import turtle
import math
def drawOctagon(tt, edgeLen, cx, cy):
    tt.up()
    tt.goto(cx - edgeLen / 2, cy - round(edgeLen * (1 + math.sqrt(2)) / 2))
    tt.down()

    tt.begin_fill()
    for i in range(8):
        tt.forward(edgeLen)
        tt.left(45)
    tt.end_fill()
    tt.hideturtle()

def stampTurt(turt, cx, cy):
    turt.up()
    turt.goto(cx -2, cy)
    turt.down()
    turt.stamp()

win = turtle.Screen()
win.bgcolor("darkorange")

turtleA = turtle.Turtle()
turtleA.speed(6)
turtleA.color("navy")

turtleB = turtle.Turtle()
turtleB.speed(6)
turtleB.color("darkorange")

turtleC = turtle.Turtle()
turtleC.speed(6)
turtleC.color("navy")

turtleD = turtle.Turtle()
turtleD.speed(6)
turtleD.color("darkorange")

turtleE = turtle.Turtle()
turtleE.speed(6)
turtleE.color("navy")
turtleE.shape("turtle")

drawOctagon(turtleA, 100, 0,0)
drawOctagon(turtleB, 64, 0, 0)
drawOctagon(turtleC, 36, 0,0)
drawOctagon(turtleD, 18, 0,0)
stampTurt(turtleE, 0,0)

drawOctagon(turtleA, 100,0,250)
drawOctagon(turtleB, 64, 0, 250)
drawOctagon(turtleC, 36, 0,250)
drawOctagon(turtleD, 18, 0,250)
stampTurt(turtleE, 0, 250)

drawOctagon(turtleA, 100, 0,-250)
drawOctagon(turtleB, 64, 0, -250)
drawOctagon(turtleC, 36, 0,-250)
drawOctagon(turtleD, 18, 0,-250)
stampTurt(turtleE, 0, -250)

drawOctagon(turtleA, 100, 250,250)
drawOctagon(turtleB, 64, 250, 250)
drawOctagon(turtleC, 36, 250,250)
drawOctagon(turtleD, 18, 250,250)
stampTurt(turtleE, 250, 250)

drawOctagon(turtleA, 100, -250,250)
drawOctagon(turtleB, 64, -250, 250)
drawOctagon(turtleC, 36, -250,250)
drawOctagon(turtleD, 18, -250,250)
stampTurt(turtleE, -250, 250)

drawOctagon(turtleA, 100, 250,0)
drawOctagon(turtleB, 64, 250, 0)
drawOctagon(turtleC, 36, 250,0)
drawOctagon(turtleD, 18, 250,0)
stampTurt(turtleE, 250, 0)

drawOctagon(turtleA, 100, -250,0)
drawOctagon(turtleB, 64, -250, 0)
drawOctagon(turtleC, 36, -250,0)
drawOctagon(turtleD, 18, -250,0)
stampTurt(turtleE, -250, 0)

drawOctagon(turtleA, 100, 250,-250)
drawOctagon(turtleB, 64, 250, -250)
drawOctagon(turtleC, 36, 250,-250)
drawOctagon(turtleD, 18, 250,-250)
stampTurt(turtleE, 250, -250)

drawOctagon(turtleA, 100, -250,-250)
drawOctagon(turtleB, 64, -250, -250)
drawOctagon(turtleC, 36, -250,-250)
drawOctagon(turtleD, 18, -250,-250)
stampTurt(turtleE, -250, -250)

win.exitonclick()