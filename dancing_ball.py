import random,time,math,turtle

p = turtle.Turtle()
scr = turtle.Screen()
p.speed(100)
scr.bgcolor("black")

def draw_circle():
    p.up()                #x cord                   #y cord
    p.goto(random.randint(-350,350),random.randint(-350,350))  #random pos on screen
   
    #random colour for circle
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    scr.colormode(255)
    p.color(r,g,b)
    
    #draw the circle
    p.begin_fill()
    p.down()
    p.circle(random.randint(10,100))           #pick random radius
    p.up()
    p.end_fill()
    p.hideturtle()

#initial delay in sec
delay = 0.5
start_time = time.time()
#for loop to draw circle with decrease delay
for i in range(50):
    draw_circle()
    time.sleep(delay)
    p.clear()
    delay = max(0.01,delay - 0.05)

end_time = time.time()    
elapsed_time = round(end_time - start_time,2)
p.up()
p.goto(0,0)
p.color("yellow")
p.write(f'TOTAL ANIMATION TIME = {elapsed_time}seconds',align = "center", 
        font = ("arial",15,"bold"))
        
time.sleep(2)
print(f'TOTAL ANIMATION TIME = {elapsed_time}seconds')

turtle.done()  #will keep window open until user closes it
