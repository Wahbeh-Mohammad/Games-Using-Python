# Libraries
import turtle as tr
import random as r


# Screen Configuration
wn = tr.Screen()
wn.title("Ping Po(ggers)ng ")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) # Stop the Screen from auto-updating

# Game Config
score_A = 0
score_B = 0

# Paddle Component Configs
Speed = 0
Shape = "square"
Color = "white"
Ball_shape = 'circle'

# Paddle A
pad_a = tr.Turtle()
pad_a.speed(Speed)
pad_a.shape(Shape)
pad_a.shapesize(stretch_wid=5,stretch_len=.3)
pad_a.color(Color)
pad_a.penup()
pad_a.goto(-350,0)

# Paddle B
pad_b = tr.Turtle()
pad_b.speed(Speed)
pad_b.shape(Shape)
pad_b.shapesize(stretch_wid=5,stretch_len=0.3)
pad_b.color(Color)
pad_b.penup()
pad_b.goto(350,0)

# Ball
ball = tr.Turtle()
ball.speed(Speed)
ball.shape(Ball_shape)
ball.color(Color)
ball.penup()
ball.goto(0,0)
x_dx = 0.5 * (r.choice([-1,1]))
y_dy = 0.5 * (r.choice([-1,1]))

# Pen
pen = tr.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,265)
pen.write("Player A: 0  Player B: 0",align='center',font=("Courier",24,'normal'))

# Functions
def startingmove():
    global x_dx,y_dy
    x_dx = 0.5 * (r.choice([-1,1]))
    y_dy = 0.5 * (r.choice([-1,1]))


def paddle_a_up():
    Y = pad_a.ycor()
    if Y<200:
        Y += 20
    pad_a.sety(Y)

def paddle_a_down():
    Y = pad_a.ycor()
    if Y>-200:
        Y -= 20
    pad_a.sety(Y)

def paddle_b_up():
    Y = pad_b.ycor()
    if Y<200:
        Y += 20
    pad_b.sety(Y)

def paddle_b_down():
    Y = pad_b.ycor()
    if Y>-200:
        Y -= 20
    pad_b.sety(Y)

# Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

# Main Game Loop
while True:
    wn.update() # Update Screen Manually
    
    # Moving the ball
    ball.setx(ball.xcor()+x_dx)
    ball.sety(ball.ycor()+y_dy)
    # Upper & Lower Border Check
    if ball.ycor()>290:
        y_dy *= -1
    if ball.ycor()<-290:
        y_dy *= -1
        
    # Right & Left Border Check
    if ball.xcor()>350:
        startingmove()
        ball.goto(0,0)
        score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A,score_B),align='center',font=("Courier",24,'normal'))

    if ball.xcor()<-350:
        startingmove()
        ball.goto(0,0)
        score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A,score_B),align='center',font=("Courier",24,'normal'))
        
    # Collision Checks
    if ball.xcor() < -340 and ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50:
        x_dx *= -1 
    elif ball.xcor() > 340 and ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50:
        x_dx *= -1








