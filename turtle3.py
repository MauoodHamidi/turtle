from turtle import *

body=Turtle()
body.color("blue")
body.shape("square")
body.shapesize(3,6)
body.penup()

wheela=Turtle()
wheela.shape("circle")
wheela.shapesize(2)
wheela.penup()

wheelb=Turtle()
wheelb.shape("circle")
wheelb.shapesize(2)
wheelb.penup()

for count in range(0,200,10):
    body.goto(count,0)
    wheela.goto(-35+count, -30)
    wheelb.goto(35+count, -30)

done()