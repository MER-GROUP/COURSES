from turtle import *
pencolor('aquamarine3'), pensize(2)
for x in range(-270, 301, 60):
    pendown()
    goto(x, -300)
    dot(7, 'dodgerblue3')
    penup()
    goto(0, 0)
dot(7, 'red')