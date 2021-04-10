import turtle
from time import sleep

#Setup
wn = turtle.Screen()
wn.title("Kopaná")
wn.bgcolor("green")
wn.setup(width=1200, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=7, stretch_len=1.5)
paddle_a.penup()
paddle_a.goto(-400, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=7, stretch_len=1.5)
paddle_b.penup()
paddle_b.goto(400, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(2, 2)
ball.penup()
ball.goto(0, 0)
#delta x and y
ball.dx = 1.2
ball.dy = 1.2

#Field
field = turtle.Turtle()
field.speed(0)
field.color("white")
field.pensize(7)
field.penup()
field.hideturtle()
field.goto(-580, -280)

#Create rectangle
def rect(delka, sirka):
    field.pendown()
    for i in range(2):
        field.fd(delka)
        field.lt(90)
        field.fd(sirka)
        field.lt(90)
    field.penup()

#Reset game
def res_game():
    ball.goto(0, 0)
    ball.dx *= -1
    pen.clear()
    pen.write("Hráč A: {}  Hráč B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
    paddle_a.goto(-400, 0)
    paddle_b.goto(400, 0)
    wn.update()

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Hráč A: 0  Hráč B: 0", align="center", font=("Courier", 24, "bold"))

#Score
score_a = 0
score_b = 0

#Moving
def paddle_a_up():
    paddle_a.up = True

def paddle_a_rel_up():
    paddle_a.up = False

def paddle_a_down():
    paddle_a.down = True

def paddle_a_rel_down():
    paddle_a.down = False

def paddle_b_up():
    paddle_b.up = True

def paddle_b_rel_up():
    paddle_b.up = False

def paddle_b_down():
    paddle_b.down = True

def paddle_b_rel_down():
    paddle_b.down = False

#Keyboard input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeyrelease(paddle_a_rel_up, "w")
wn.onkeyrelease(paddle_a_rel_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeyrelease(paddle_b_rel_up, "Up")
wn.onkeyrelease(paddle_b_rel_down, "Down")

#Draw field
rect(580*2,280*2)
field.goto(-580,-140)
rect(100,280)
field.goto(580,140)
rect(-100,-280)
field.goto(0,-40)
field.pendown()
field.circle(40)
field.penup()
field.goto(0,280)
field.pendown()
field.goto(0,-280)

wn.update()
sleep(1)

#Game loop
while True:
    wn.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Paddle movement
    if paddle_a.up == True:
        if paddle_a.ycor() < 210:
            paddle_a.sety(paddle_a.ycor() + 0.9)
    
    if paddle_a.down == True:
        if paddle_a.ycor() > -210:
            paddle_a.sety(paddle_a.ycor() - 0.9)

    if paddle_b.up == True:
        if paddle_b.ycor() < 210:
            paddle_b.sety(paddle_b.ycor() + 0.9)
    
    if paddle_b.down == True:
        if paddle_b.ycor() > -210:
            paddle_b.sety(paddle_b.ycor() - 0.9)

    #Walls
    if ball.ycor() > 260:
        ball.sety(260)
        ball.dy *= -1

    if ball.ycor() < -260:
        ball.sety(-260)
        ball.dy *= -1
    
    if ball.xcor() > 560:
        ball.setx(560)
        ball.dx *= -1

    if ball.xcor() < -560:
        ball.setx(-560)
        ball.dx *= -1

    #Paddle interactions
    if (ball.xcor() > 373 and ball.xcor() < 400) and (ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() - 70):
        ball.setx(363)
        ball.dx *= -1
    
    if (ball.xcor() < -373 and ball.xcor() > -400) and (ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() - 70):
        ball.setx(-363)
        ball.dx *= -1

    #Goal
    if (ball.xcor() > 495 and ball.xcor() < 580) and (ball.ycor() < 125 and ball.ycor() > -125):
        score_a += 1
        res_game()
        if score_a >= 11 or score_b >= 11:
            break
        sleep(1)


    if (ball.xcor() < -495 and ball.xcor() > -580) and (ball.ycor() < 125 and ball.ycor() > -125):
        score_b += 1
        res_game()
        if score_a >= 11 or score_b >= 11:
            break
        sleep(1)

wn.clear()
wn.bgcolor("black")
pen.color("white")
pen.goto(0, 0)
if score_a >= 11:
    pen.write("The winner is player A!", align="center", font=("Courier", 35, "bold"))
elif score_b >= 11:
    pen.write("The winner is player B!", align="center", font=("Courier", 35, "bold"))
sleep(5)