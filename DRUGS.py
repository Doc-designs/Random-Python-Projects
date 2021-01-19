#turtle graph game
import turtle

#screen
turtle.setup(1000,700)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("DRUGS")

#Bong
Bong1 = turtle.Turtle()
Bong1.color("green")
Bong1.shape("circle")
Bong1.shapesize(10,10)
Bong1.penup()
Bong1.setpos(0,-200)


Bong2 = turtle.Turtle()
Bong2.color("lightgray")
Bong2.shape("square")
Bong2.shapesize(2.5,0.5)
Bong2.penup()
Bong2.setpos(110,-150)
Bong2.setheading(-45)


Bong3 = turtle.Turtle()
Bong3.color("lightgrey")
Bong3.shape("circle")
Bong3.shapesize(1,2)
Bong3.penup()
Bong3.setpos(130,-130)


Bong4 = turtle.Turtle()
Bong4.color("green")
Bong4.shape("square")
Bong4.shapesize(10,5)
Bong4.penup()
Bong4.setpos(0,-40)


Smoke = turtle.Turtle()
Smoke.color("grey")
Smoke.shape("circle")
Smoke.shapesize(4,4)
Smoke.penup()
Smoke.setpos(0,100)
#def
def Smoke1():
    Smoke1 = turtle.Turtle()
    Smoke1.color("grey")
    Smoke1.shape("circle")
    Smoke1.penup()
    Smoke1.setpos(0,300)


#Smoking
turtle.listen()
turtle.onkey(Smoke1,"S")










delay = raw_input("press enter to finish")
