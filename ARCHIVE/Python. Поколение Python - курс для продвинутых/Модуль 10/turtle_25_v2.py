from turtle import *

olimpic_colors = ('cyan', 'yellow', 'black', 'green', 'red')
pensize(6)
speed(0)

def color_circle(color, R):
    pencolor(color)
    circle(R) 

def olimpic(colors, R):
    color_num = 0
    j = 0
    k = -130    
    for i in range(-R*2, R*2 + 1, R):
        penup()
        goto(i, j)
        pendown()
        color_circle(colors[color_num], R)
        color_num += 1
        j, k = k, j

olimpic(olimpic_colors, 100)
done()