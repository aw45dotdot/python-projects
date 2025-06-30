import turtle,random, time

scr = turtle.Screen()

scr.bgcolor("yellow")
#width and height of screen
scr.setup(500,500)
#turn off screen update
scr.tracer(0)
#player
p = turtle.Turtle()
p.shape("triangle")
p.color("red")



#score display
score = 0
scor_disp = turtle.Turtle()
scor_disp.hideturtle()
scor_disp.color("black")
scor_disp.write(f"Score: {score}",font=('Calibri',20,'bold'))
scor_disp.penup()
scor_disp.goto(250,300)

balloons = []
#game varaible
game_speed = 0.05
dif_inc = 0.005
spawn_interval = 2
last_spawn_time = time.time()
runnning = True

#functions
def move_left():
    pass

def move_right():
    pass

def ballons_spawn():
    pass

def update_score(points):
    pass

def game_over():
    pass

#keybinding
scr.listen()
scr.onkey(move_right,"a")
scr.onkey(move_left,"d")
#game loop using while loop
