import turtle

def spiral(turt, length):
    win = turtle.Screen()
    turt = turtle.Turtle()
    if length > 0:
        turt.fd(length)
        turt.right(90)
        for i in range(2):
            spiral(turt,length-5)
    else:
        pass

sc = turtle.Screen()
alex = turtle.Turtle()
spiral(alex,100)
sc.exitonclick()