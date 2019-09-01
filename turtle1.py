from turtle import *
import random

#get input from the user on their name, the colours they want and whether the rocket will take off
print("Hello, welcome to the Rocket creator. Here you will select the colours for your rocket.")
name = input("First, please tell me your name.     ")
shiptopColour = input("Thank you, %s. Now please tell me the colour you would like for the top of your rocket." %(name))
shipbottomColour = input("Thank you. Now please tell me the colour you would like for the bottom of your rocket.")
shipboostersColour = input("Thank you. Now please tell me the colour you would like for the boosters of your rocket.")
print("Thank you. So the top of your rocket will be %s, the bottom of your rocket will be %s, and your boosters will be %s." %(shiptopColour, shipbottomColour, shipboostersColour))
takeOff = input("%s, would you like your rocket to take off? y or n" %(name))
print("Here is your rocket. I hope you like it :)")


def writing():
    #code for the writing
    writer = Turtle()
    writer.hideturtle()
    writer.color("black")
    writer.penup()
    writer.goto(-200,-200)
    writer.pendown()
    writer.write("This rocket was made by: "+ name)
    #writer.write(name)

writing()

#code for the bottom of the ship
shipbottom = Turtle()
shipbottom.shape("square")
shipbottom.shapesize(10,5,1)
shipbottom.color(shipbottomColour)
#bgcolor('#%06X' % random.randint(0,256**3-1))
bgcolor("white")
shipbottom.penup()
shipbottom.goto(0,-50)

#code for the top of the ship
shiptop = Turtle()
shiptop.shape("triangle")
shiptop.shapesize(5,5,1)
shiptop.color(shiptopColour)
shiptop.penup()
shiptop.goto(0,80)
shiptop.right(30)

#code for the left rocket booster
shipbooster1 = Turtle()
shipbooster1.shape("square")
shipbooster1.shapesize(8,2,10)
shipbooster1.color(shipboostersColour)
shipbooster1.penup()
shipbooster1.goto(-70,-80)
shipbooster1.pendown()

#code for the right rocket booster
shipbooster2 = Turtle()
shipbooster2.shape("square")
shipbooster2.shapesize(8,2,10)
shipbooster2.color(shipboostersColour)
shipbooster2.penup()
shipbooster2.goto(70,-80)
shipbooster2.pendown()

#flame colour
flamecolor = "red"

#code for the left flame
flame1 = Turtle()
flame1.shape("turtle")
flame1.color(flamecolor)
flame1.penup()
flame1.hideturtle()
flame1.goto(70,-170)
flame1.speed("fastest")
flame1.pendown()

#code for the left flame
flame2 = Turtle()
flame2.shape("turtle")
flame2.color(flamecolor)
flame2.penup()
flame2.hideturtle()
flame2.goto(-70,-170)
flame2.speed("fastest")
flame2.pendown()

#code for the takeoff
#print ('#%06X' % random.randint(0,256**3-1))
if (takeOff=="y"):
    for i in range(0, 200, 10):
        shipbottom.goto(0, -50+i)
        shiptop.goto(0, 80+i)
        shipbooster1.goto(-70,-80+i)
        shipbooster2.goto(70,-80+i)
        flame1.circle(10)
        flame1.goto(70,-170+i)
        flame2.circle(10)
        flame2.goto(-70,-170+i)
elif (takeOff=="n"):
    print("You chose not to take off.")
else:
    print("Sorry, you did not choose 'n' or 'y'. Please try again if you want it to take off.")

done()