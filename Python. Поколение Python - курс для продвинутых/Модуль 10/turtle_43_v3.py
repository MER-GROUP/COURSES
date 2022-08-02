import turtle, random

turtle.Screen().setup(500, 500)
turtle.Screen().bgcolor('black')
turtle.Screen().colormode(255)
turtle.speed(0)

def left_mouse_click(x, y):
  star(x, y)

def star(x, y):
  turtle.penup()
  turtle.setpos(x, y)
  turtle.pendown()
  n = random.randint(3, 10)
  # n = 3
  size = random.randint(5, 10)
  # size = 30
  color = (random.randrange(256), random.randrange(256), random.randrange(256))
  turtle.setheading(random.randint(0, 361))
  turtle.fillcolor(color)
  turtle.begin_fill()
  if n > 3:
    for i in range(n):
      turtle.forward(size)
      turtle.right(180 - 360 / 2 / n)
      turtle.forward(size)
      turtle.left(180 - 360 / n * 1.5)
  else:  
    for i in range(n):
      turtle.forward(size)
      turtle.right(180 - 360 / 4 / n)
      turtle.forward(size)
      turtle.left(180 - 360 / n * 1.25)
  turtle.end_fill()
    
turtle.Screen().listen()
turtle.hideturtle()
turtle.Screen().onclick(left_mouse_click)
turtle.done()