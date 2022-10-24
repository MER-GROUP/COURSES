import turtle as t
import math

t.ht()
t.speed(0)
t.tracer(500, 0)
m = 0.5
t.colormode(255)

l = [('Солнце', 100, 'yellow'),
    ('Меркурий', 30, 'orange'),
    ('Венера', 40, 'orange'),
    ('Земля', 30, [(0, 255, 0), (0, 0, 255)]),
    ('Марс', 25, 'red'),
    ('Юпитер', 50, 'orange'),
    ('Сатурн', 50, 'orange'),
    ('Уран', 45, 'cyan'),
    ('Нептун', 45, [(0, 150, 150), (0, 30, 5)]),
    ('Плутон', 25, 'brown')
    ]

def ellipse(a, b):
    """
    This function from https://barzunov.ru/2019/11/turtle-draw-ellipse/
    """
    dx = t.xcor()
    dy = t.ycor()
    for deg in range(361):
        rad = math.radians(deg)
        x = a * math.sin(rad) + dx
        y = -b * math.cos(rad) + b + dy
        t.goto(x, y)

def crl(a, b):
    t.penup()
    t.goto(b + a[1] * m, -(a[1] * m))
    t.pendown()

    if a[0] in ['Земля', 'Нептун']:
        for i in range(-int(a[1] * m), int(a[1] * m + 1)):
            for k in range(2):
                t.goto(b + a[1] * m, i)
                t.pendown()
                x = ((a[1]*m)**2 - i**2)**0.5
                for j in range(int(x) + 1):
                    col1 = (a[2][1][0] - a[2][0][0]) / a[1]
                    col2 = (a[2][1][1] - a[2][0][1]) / a[1]
                    col3 = (a[2][1][2] - a[2][0][2]) / a[1]
                    t.pencolor(int(a[2][0][0] + col1 * j), int(a[2][0][1] + col2 * j), int(a[2][0][2] + col3 * j))
                    t.fd(1)
                t.penup()
                t.left(180)
        t.goto(b + a[1] * m, -(a[1] * m))
        t.pencolor('black')
        t.pendown()
        t.circle(a[1] * m)
    else:
        t.fillcolor(a[2])
        t.begin_fill()
        t.circle(a[1] * m)
        t.end_fill()

    t.penup()
    t.goto(b + a[1] * m, -20-(a[1] * m))
    t.fillcolor('black')
    t.write(a[0], False, 'center', ('Arial', 10, 'normal'))

    if a[0] == 'Сатурн':
        t.goto(b + a[1] * m, 0 - 15)
        t.pendown()
        ellipse(30, 15)
        t.penup()
    return a[1] * m * 2

b = -300
for i in l:
    b += crl(i, b) + 20

t.done()