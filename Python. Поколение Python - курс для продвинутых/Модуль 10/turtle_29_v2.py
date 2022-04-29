import turtle as t

color = ('brown', 'blue')
t.hideturtle()
t.penup()
t.goto(125, 0)
t.pendown()
for i in range(2):
    t.fillcolor(color[i])
    t.begin_fill()
    for _ in range(3):
        if not i:
            t.left(120)
            t.forward(250)
        else:
            t.right(90)
            t.forward(180)
    t.end_fill()
    t.back(35)

t.done()