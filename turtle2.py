from turtle import *
myTurtle=Turtle()

def square():
    myTurtle.begin_fill()
    for count in range(4):
        myTurtle.fd(100)
        myTurtle.rt(90)
    myTurtle.end_fill()

myTurtle.color("red")
square()

myTurtle.rt(90)
myTurtle.fd(100)
myTurtle.lt(90)

myTurtle.color("green")
square()

done()
