'''
Ok. Так как  circle умеет рисовать правильные многоугольники, то используем это. 
'''
import turtle
turtle.rt(22.5)
turtle.pensize(10)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100, 360, 8)
turtle.end_fill()
turtle.setpos(4, 10)
turtle.pencolor('white')
turtle.circle(90, 360, 8)
turtle.penup()
turtle.setpos(40, 60)
turtle.write('STOP', align='center', font=('Arial', 40, 'bold'))
turtle.done()