from turtle import *
from random import randint

ZOOM = 0.6
PITCH = 18
planets = (('Солнце', 1390, 'yellow'),
           ('Меркурий', 4.8794, '#8A8784'),
           ('Венера', 12.1036, '#D08824'),
           ('Земля', 12.742, '#6082CA'),
           ('Марс', 6.78, '#BF9A76'),
           ('Юпитер', 139.822, '#BAB9C3'),
           ('Сатурн', 116.464, '#D9AB47'),
           ('Уран', 50.724, '#60BDEE'),
           ('Нептун', 49.244, '#4C6DED'),
           ('Плутон', 2.3766, '#5B5D5A'))

def ellipse(rad):
    for i in range(2):
        circle(rad - 90, 90)
        circle(rad // 2 - 90, 90)

Screen().setup(1000, 400)
Screen().colormode(255)
Screen().bgcolor('black')
speed(0)
ht()
x = -2050
pencolor('white')
penup()
goto(77, -70)
pendown()
ellipse(220)
for _ in range(50):
    penup()
    goto(randint(0, 999) - 500, randint(0, 399) - 200)
    pendown()
    circle(0.5)
for p in planets:
    penup()
    x += p[1] * ZOOM + PITCH
    goto(x, -p[1] * ZOOM)
    pendown()
    fillcolor(p[2])
    pencolor(p[2])
    begin_fill()
    circle(p[1] * ZOOM)
    end_fill()
    penup()
    goto(x, -p[1] * ZOOM - PITCH)
    pendown()
    pencolor('white')
    write(p[0], move=False, align='center', font=('Arial', 8, 'normal'))
    x += p[1] * ZOOM + PITCH
done()