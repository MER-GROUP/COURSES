import turtle
import math
def polygon(size, color):
    turtle.penup()
    turtle.setposition(-size * math.tan(math.pi / 8), -size)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size, steps = 8)
    turtle.end_fill()
    
turtle.right(180 / 8)
polygon(200, 'black')
polygon(190, 'white')
polygon(180, 'red')
turtle.penup()
turtle.setposition(0, -50)
turtle.fillcolor('white')
turtle.write('STOP', align = 'center', font = ('Times new roman', 90, 'normal'))
turtle.done()