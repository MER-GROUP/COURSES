import turtle
import random

def star(l, n, x, y, c):
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(2)
    turtle.colormode(255)
    turtle.Screen().colormode(255)
    turtle.Screen().bgcolor('LightCyan')
    turtle.pencolor(c)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(n)
    turtle.pendown()
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(5):
        turtle.right(180 - 180 / 5)
        turtle.fd(l)
    turtle.end_fill()


for _ in range(100):
    l = random.randrange(20, 70)
    n = random.randrange(0, 360)
    x = random.randrange(-300, 300)
    y = random.randrange(-300, 300)
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    star(l, n, x, y, c)
turtle.done()