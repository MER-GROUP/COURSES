import turtle as t
from math import sin, cos, radians
from random import randrange as rnd

t.Screen().bgcolor('black')
t.Screen().colormode(255)
t.hideturtle()
t.speed(0)


def random_color():
    return rnd(256), rnd(256), rnd(256)


def star_uneven(obj, beams, figures, i, coors, r, col):
    angle = 360 / beams / figures * i
    obj.right(angle)
    x_start = coors[0] - r * cos(radians(180 / beams / 2 + angle))
    y_start = coors[1] + r * sin(radians(180 / beams / 2 + angle))

    w = 2 * r * cos(radians(180 / beams / 2))
    obj.up()
    obj.goto(x_start, y_start)
    obj.down()
    obj.color(col)
    obj.begin_fill()
    for i in range(beams):
        obj.forward(w)
        obj.right(180 - 180 / beams)
    obj.end_fill()
    obj.setheading(0)


def square(obj, beams, figures, i, coors, r, col):
    angle = 360 / beams / figures * i
    obj.right(angle)
    x_start = coors[0] - r * cos(radians(45 + angle))
    y_start = coors[1] + r * sin(radians(45 + angle))

    w = 2 * r / 2 ** 0.5
    obj.up()
    obj.goto(x_start, y_start)
    obj.down()
    obj.color(col)
    obj.begin_fill()
    for i in range(4):
        obj.forward(w)
        obj.right(90)
    obj.end_fill()
    obj.setheading(0)


def star(obj, beams, coors, r, col):
    count = 0
    while beams % 2 == 0 and beams != 4:
        beams //= 2
        count += 1

    func = square if beams == 4 else star_uneven

    figures = 2 ** count
    for i in range(figures):
        func(obj, beams, figures, i, coors, r, col)


def left_mouse_click(x, y):
    star(t, beams=rnd(5, 33), coors=(x, y), r=rnd(15, 40), col=random_color())


t.Screen().onclick(left_mouse_click)
t.Screen().listen()

t.done()