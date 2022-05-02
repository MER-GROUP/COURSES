import turtle

turtle.Screen().bgcolor('white')

for _ in range(3):
  turtle.forward(120)
  turtle.left(120)
  
  
turtle.penup()
turtle.goto(0, 80)
turtle.fillcolor('white')
turtle.pencolor('white')
turtle.begin_fill()

for _ in range(3):
  turtle.dot(30, 'black')
  turtle.forward(120)
  turtle.right(120)

turtle.end_fill()
turtle.done()