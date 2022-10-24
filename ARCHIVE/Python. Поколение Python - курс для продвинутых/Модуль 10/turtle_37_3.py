import turtle

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.shape('square')
turtle.shapesize(2)
step = 2 * turtle.get_shapepoly()[0][0]

for i in range(-2, 3):
    for j in range(-2, 3):
        turtle.fillcolor('white' if (i + j) % 2 else 'black')
        turtle.setpos(j * step, i * step)
        turtle.stamp()

turtle.done()