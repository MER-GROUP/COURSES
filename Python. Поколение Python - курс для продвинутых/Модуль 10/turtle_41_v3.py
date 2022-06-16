import turtle as t, random as ran
t.Screen().setup(600, 600)
t.Screen().colormode(255)
t.speed(0)
t.Screen().bgcolor('darkblue')
def window():
    col = ran.choice(['yellow', 'white'])
    fill(col)
    begin()
    for _ in range(4):
        t.forward(20)
        t.left(90)
    end()
    t.right(90)
    t.forward(30)
    t.left(90)

def star():
    t.pensize(ran.randint(1, 5))
    up()
    t.goto(ran.randint(-300, 300), ran.randint(0, 300))
    color('white')
    t.dot()

def hous():
    x, y = t.pos()
    a, b = ran.randint(200, 500), ran.randint(40, 80)
    fill('blue')
    begin()
    for _ in range(2):
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.left(90)
    end()
    win = ran.randint(0, 2)
    t.goto(ran.randint(x, (x + b // 3)), ran.randint(y, (y + a - 20)))
    for _ in range(win):
        window()
    t.goto(x + b, y)

up, down, color = t.up, t.down, t.pencolor
fill, begin, end = t.fillcolor, t.begin_fill, t.end_fill
[star() for _ in range(ran.randint(50, 100))]
t.goto(-300, -300)
z = t.xcor()
while z <= 300:
    hous()
    z = t.xcor()
t.done()