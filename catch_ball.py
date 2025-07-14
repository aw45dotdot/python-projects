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
running = True

#functions
def move_left():
    x = p.xcor()-20
    if x > -240:
        p.set(x)

def move_right():
    x = p.xcor()+20
    if x < +240:
        p.set(x)

def ballons_spawn():
    ballon = turtle.Turtle()
    ballon.up()
    ballon.shape("circle")
    ballon.color(random.choice(["red", "blue", "green", "purple", "orange"]))
    ballon.goto(random.randint(-250,250),random.randint(-250,250))
    ballon.speed = random.uniform(1,10)
    if random.random()<0.2:
        ballon.color('black')
        ballon.is_bomb = True
    else:
        ballon.is_bomb = False
    balloons.append(ballon)

def update_score(points):
   global score
   score = (points + score)
   scor_disp.clear()
   scor_disp.write(f'score:{score}',font=('Calibri',20,'bold'))
   
   

def game_over():
    global running
    running = False
    gme_ovr_disp = turtle.Turtle()
    gme_ovr_disp.hideturtle()
    gme_ovr_disp.color("green",font=('Calibri',20,'bold'),align='centre')
    scr.update()
    time.sleep(3)
    scr.bye()

#keybinding
scr.listen()
scr.onkey(move_right,"a")
scr.onkey(move_left,"d")
#game loop using while loop

while running:
    scr.update()
    current_time = time.time()
    if current_time - last_spawn_time > spawn_interval:
        ballons_spawn
        last_spawn_time = current_time

    for ballon in balloons[:]:
        ballon.sety(ballon.ycor() - ballon.speed)
        if ballon.ycor() < -250:
            ballon.remove(ballon)
            ballon.hideturtle()
        if p.distance(ballon) < 30:
            if ballon.is_bomb:
                game_over()
            else:
                update_score(10)
            ballon.remove(ballon)
            ballon.hideturtle()
    game_speed = max(0.005, game_speed - dif_inc)
    spawn_interval = max(0.5, spawn_interval - 0.0005)
    time.sleep(game_speed)
