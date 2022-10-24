from turtle import *
from random import randint
from math import tan, sqrt, radians

square = 4000

def draw_figure(n):
    size = sqrt(4 * square * tan(radians(180 / n)) / n)
    fillcolor(tuple((randint(0, 255) for _ in range(3))))
    begin_fill()
    forward(size / 2)
    left(360 / n)
    for i in range(n - 1):
        forward(size)
        left(360 / n)
    forward(size / 2)
    end_fill()

Screen().colormode(255)
Screen().bgcolor('white')
Screen().setup(640, 480)
Screen().tracer(1, 0)
speed(0)
ht()
for x in range(5):
    for y in range(5):
        penup()
        goto(x * 100 - 200, y * 100 - 200)
        pendown()
        draw_figure(randint(3, 8))
done()