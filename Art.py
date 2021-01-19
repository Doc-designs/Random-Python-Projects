#turtle graph game
import turtle

#screen
turtle.setup(1000,700)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Art")

#player
player = turtle.Turtle()
player.color("blue")
player.shape("arrow")
player.size(5)
player.pendown()
player.speed(0)

#speed
speed = 1

#define Functions
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def superspeed():
    global speed
    speed = 1
    speed += 1
def normalspeed():
    global speed
    speed = 2
    speed -= 1
def slowspeed():
    global speed
    speed = 1
    speed -= 0
def red():
    player.pencolor("red")
    player.color("red")
#Key Bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(superspeed, "Up")
turtle.onkey(normalspeed, "Down")
turtle.onkey(slowspeed, "p")
turtle.onkey(red, "r")
while True:
    player.forward(speed)





















delay = raw_input("press enter to finish")

