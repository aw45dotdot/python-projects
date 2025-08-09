import random
import turtle
import time

scr = turtle.Screen()
scr.setup(width = 600, height = 600)
#scr.tracer(0)
scr.bgcolor("black")

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.up()
paddle.goto(0,-350)
paddle_width= 150


ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.up()
ball.goto(0,0)
ball.dx= 2
ball.dy= -2

bricks = []
colours = ["red", "orange", "yellow", "green"]

for row in range(4):
    for col in range(-270,300,80):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colours[row])
        brick.up()
        brick.speed(0)
        brick.goto(col,150-(row*30))
        bricks.append(brick)

#score
score = 0
scor_disp = turtle.Turtle()
scor_disp.color("white")
scor_disp.up()
scor_disp.goto(400,200)
scor_disp.down()
scor_disp.write(f'Score:{score}',align="left",font=("Calibri",20,"bold"))
scor_disp.hideturtle()

#paddle movement
def pad_left():
    x = paddle.xcor()
    if x - paddle_width//2 > -290:
        paddle.setx(x-20)
    
def pad_right():
    x = paddle.xcor()
    if x + paddle_width//2 < 290:
        paddle.setx(x+20)

#keyboard functions
scr.listen()
scr.onkey(pad_left, "a")
scr.onkey(pad_right, "d")

#game start flag
game_start = False

def start_game(x,y):
    global game_start
    game_start = True

scr.onclick(start_game)

#game loop
while True:
    scr.update(0)
    time.sleep(0.1)
    
    if not game_start:
        continue
    
    #moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #ball collision with wall
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= (-1)

    if ball.ycor() > 290:
        ball.dy *= (-1)
    
    if ball.ycor() > -290:
        ball.goto(0,0)
        ball.dy *= (-1)
        game_start = False
        score = 0
        scor_disp.clear()
        scor_disp.write(f'Score:{score}',align="left",font=("Calibri",20,"bold"))

    #ball coliding with paddle
    if (ball.ycor() > 290 and ball.ycor() < 290) and (paddle.xcor() - 75 < ball.xcor() , paddle.xcor() + paddle_width - 75):
        ball.dy *= (-1)
    
    #ball collision with bricks
    for brick in bricks:
        if abs(ball.xcor() - brick.xcor()) < 15 and abs(ball.ycor() - brick.ycor()) < 15:
            ball.dy*=(-1)
            brick.hideturtle()
            bricks.remove(brick)
            score += 1
            scor_disp.clear()
            scor_disp.write(f'Score:{score}',align="left",font=("calibri",20,"bold"))

    if not bricks:
        print("YOU WIN")
        break
