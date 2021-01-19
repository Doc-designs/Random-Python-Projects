#turtle graph game
import turtle

#screen
turtle.setup(1000,700)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tag")
#boarder turtle create
boarder = turtle.Turtle()
boarder.penup()
boarder.setpos(-300,-300)
boarder.pendown()
boarder.pensize(3)

#Draw boarder
for side in range(4):
    boarder.forward(600)
    boarder.left(90)
    boarder.hideturtle()

#player
player = turtle.Turtle()
player.color("blue")
player.shape("arrow")
player.penup()
player.speed(0)

#enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("arrow")
enemy.penup()
enemy.speed(0)
enemy.setpos(250,250)
#enemy movement

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
#Key Bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(superspeed, "Up")
turtle.onkey(normalspeed, "Down")
while True:
    player.forward(speed)

    #boundary's
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)

    #boundary's
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)




















delay = raw_input("press enter to finish")
