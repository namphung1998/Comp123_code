import turtle

# Your job in this question is to write a function named
# drawSquares. The drawSquares draws a series of squares
# each one next to the other. The drawn squares start with
# 10 pixels to a side, and get bigger by 10 until they
# reach the input max size, after which they get smaller
# until they reach 10 again. The function has two
# parameters, a trutle object (which will be used to draw
# the squares) and a maximum size object (which should be
# a multiple of 10). This function does not need to return
# anything. See the included example output for more
# information.

def drawSquares(turt, max):
   for sideLen in range(10, max+10, 10):
       for i in range(4):
           turt.fd(sideLen)
           turt.left(90)
       turt.fd(sideLen)
       if sideLen == max:
           for len in range(max-10, 0, -10):
               for i in range(4):
                   turt.forward(len)
                   turt.left(90)
               turt.fd(len)

sc = turtle.Screen()
turt = turtle.Turtle()
drawSquares(turt, 60)
sc.exitonclick()