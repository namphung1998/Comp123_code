

# put import statements here
import turtle
import random

# Question 1
def fourStairs(tt):
    "a function to draw a set of four stairsteps"
    tt.fd(160)
    tt.left(90)
    tt.fd(100)
    tt.left(90)
    for i in range (4):
        tt.fd(40)
        tt.left(90)
        tt.fd(25)
        tt.right(90)
    tt.left(180)

sc = turtle.Screen()
bob = turtle.Turtle()

#fourStairs(bob)   #used this line to check if the function works. I did the same thing for other functions as well
#sc.exitonclick()


# put your solution here




# Question 2
def nStairs(turt, numStairs):
    "a function to draw a set of n stairsteps."
    turt.fd(40*numStairs)
    turt.left(90)
    turt.fd(25*numStairs)
    turt.left(90)
    for i in range (numStairs):
        turt.fd(40)
        turt.left(90)
        turt.fd(25)
        turt.right(90)
    turt.left(180)

win = turtle.Screen()
alex = turtle.Turtle()

#nStairs(alex, 2)
#win.exitonclick()

# put your solution here




# Question 3
def rollDice(numDice):
    "a function to simulate rolling a given number of dices"
    sum = 0
    for i in range (0, numDice):
        roll = random.randrange(1,6,1)
        sum = sum + roll
    return sum
#print(rollDice(3))
# put your solution here


# Question 4
def printNMults(mult, n):
    "a function to show the multiples of a given integer"
    result = 0
    for i in range (0,n+1):
        result = mult*i
        print(result)

#printNMults(5,10)


# put your solution here



# Question 5



# put your definition of flower here, before the petal function.
def flower (turt, numPetal, turnAngle):
    "a function to draw a flower"
    for i in range (numPetal):
        petal(turt)
        turt.right(turnAngle)

#sc = turtle.Screen()
#bob = turtle.Turtle()


def petal(bobT):
    """Takes in a turtle object, and draws a single petal in the direction the turtle is
    currently facing, and going to the left of that point"""
    bobT.begin_fill()
    bobT.forward(150)
    bobT.left(50)
    bobT.forward(40)
    bobT.left(100)
    bobT.forward(40)
    bobT.left(50)
    bobT.forward(150)
    bobT.end_fill()
    bobT.left(160)

#flower(bob, 8, 45)
#sc.exitonclick()
