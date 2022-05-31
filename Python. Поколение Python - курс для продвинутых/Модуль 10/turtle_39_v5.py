import turtle
import math

def ellipse(a, b):
    """
    This function from https://barzunov.ru/2019/11/turtle-draw-ellipse/
    """
    dx = turtle.xcor()
    dy = turtle.ycor()
    for deg in range(361):
        rad = math.radians(deg)
        x = a * math.sin(rad) + dx
        y = -b * math.cos(rad) + b + dy
        turtle.goto(x, y)
    
def planet(size, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()

r = 50
n = 10
colors = ['#ffff66','#ad5a00','#ad5a00', '#87CEEB', '#FF6347','#ad5a00','#ad5a00','#20B2AA', '#4169E1','#ad5a00']
size = [2*r, r/2.5, r/2, r/2.5, r/3, r, r, r/1.5, r/1.5, r/4.5]
canvx = 900 
canvy = 400
turtle.Screen().setup(canvx, canvy)
turtle.speed(0)
positionx = -(canvx // 2)
positiony = 0
turtle.penup()
turtle.goto(positionx, 0)
turtle.pendown()
for i in range(n):
  positionx += size[i]
  turtle.penup()
  turtle.goto(positionx, -size[i])
  turtle.pendown()
  planet(size[i], colors[i])
  if i == 6:
    turtle.penup()
    turtle.goto(positionx, -size[i]+(r/1.5)/2)
    turtle.pendown()
    ellipse(r+r*0.2, r/1.5)
  positionx += size[i] + 20

turtle.done()