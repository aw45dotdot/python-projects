import random
import turtle
import time

scr = turtle.Screen()
scr.setup(1.0,1.0)
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
