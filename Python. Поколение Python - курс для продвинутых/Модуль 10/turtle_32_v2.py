import turtle as t

def rainbow(size):
    color = ('red', 'orange', 'yellow', 'green', 'aquamarine', 'blue', 'cyan', 'DarkCyan', 'purple', 'magenta')
    t.hideturtle()
    t.speed(0)
    for i in range(10):
        t.penup()
        t.goto(0, -(size / 2) + i * (size / 10))
        t.fillcolor(color[i])
        t.begin_fill()
        t.circle(size - i * (size / 10))
        t.end_fill()

rainbow(150)
t.done()