import turtle

def draw_rectangle(length, height, r,g,b, x = 0, y = 0):
    t = turtle.Turtle()
    t.speed(300)
    t.fillcolor(r,g,b)
    t.hideturtle()
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.setx(length)
    
def get_color(color):
    if color == "red":
        return 1,0,0
    if color == "white":
        return 1,1,1
    if color == "blue":
        return 0,0,1
    else:
        return 0,0,0
    
def draw_star(size, r,g,b, x = 0, y = 0):
    t = turtle.Turtle()
    t.speed(300)
    t.pencolor(get_color("white"))
    t.up()
    turn = 144
    t.goto(x,y)
    t.fillcolor(r,g,b)
    t.hideturtle()
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(turn)
        
    t.end_fill()

def draw_flag(height):
    fly = 1.9 * float(height)
    hoist_canton = height * (7/13)
    fly_canton = fly * (2/5)
    stripe = height / 13
    star = stripe * (4/5)
    e = hoist_canton / 10
    f = fly_canton / 14
    r,g,b = get_color("red")
    draw_rectangle(fly, height, r,g,b)
    r,g,b = get_color("blue")
    draw_rectangle(fly_canton, hoist_canton, r,g,b)

   
    r,g,b = get_color("white")
    draw_rectangle(fly - fly_canton, stripe, r,g,b, fly_canton, -stripe)
    r,g,b = get_color("red")
    draw_rectangle(fly - fly_canton, stripe, r,g,b, fly_canton, -stripe * 2)
    r,g,b = get_color("white")
    draw_rectangle(fly - fly_canton, stripe, r,g,b, fly_canton, -stripe * 3)
    r,g,b = get_color("red")
    draw_rectangle(fly - fly_canton, stripe, r,g,b, fly_canton, -stripe * 4)
    r,g,b = get_color("white")
    draw_rectangle(fly - fly_canton, stripe, r,g,b, fly_canton, -stripe * 5)
    r,g,b = get_color("red")
    draw_rectangle(fly - fly_canton, stripe, r,g,b, fly_canton, -stripe * 6)
    

    r,g,b = get_color("white")    
    draw_rectangle(fly, stripe, r,g,b, 0, -hoist_canton)
    r,g,b = get_color("red")
    draw_rectangle(fly, stripe, r,g,b, 0, -hoist_canton + (-stripe))
    r,g,b = get_color("white")
    draw_rectangle(fly, stripe, r,g,b, 0, -hoist_canton + (-stripe * 2))
    r,g,b = get_color("red")
    draw_rectangle(fly, stripe, r,g,b, 0, -hoist_canton + (-stripe * 3))
    r,g,b = get_color("white")
    draw_rectangle(fly, stripe, r,g,b, 0, -hoist_canton + (-stripe * 4))
    r,g,b = get_color("red")
    draw_rectangle(fly, stripe, r,g,b, 0, -hoist_canton + (-stripe * 5))

    
    r,g,b = get_color("white")

    for i in range(1,12,2):
        for j in range(1,10, 2):
            draw_star(star, r,g,b, e * i , -f * j )

    for i in range(2,12,2):
        for j in range(2,10,2):
            draw_star(star,r,g,b, e * i, -f * j)
        
    

    
r,g,b = get_color("red")
r,g,b = get_color("blue")
draw_flag(200)
