import math
import random
import turtle


def star(x, y):
    side = random.randrange(3, 70)
    n = random.randrange(5, 10, 2)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.up()
    turtle.goto(x, y)
    turtle.left(random.randrange(380))
    turtle.down()
    color = random.randrange(256), random.randrange(256), random.randrange(256)
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(side)
        turtle.right(180 - 180 / n)
    turtle.end_fill()


def left_mouse_click(x, y):
    star(x, y)


turtle.Screen().colormode(255)
turtle.Screen().bgcolor('black')
turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()
turtle.done()