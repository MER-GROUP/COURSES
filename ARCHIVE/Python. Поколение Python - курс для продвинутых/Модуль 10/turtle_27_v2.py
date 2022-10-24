import turtle
import random
def snowflake():
  turtle.Screen().bgcolor("black")
  turtle.hideturtle()
  for j in range(random.randint(5, 25)):
    turtle.penup()
    turtle.goto(random.randrange(-200, 200), random.randrange(-200, 200))
    turtle.pendown()
    size = random.randint(2, 12)
    turtle.pensize(random.randrange(size // 2))
    turtle.pencolor(('blue', 'DarkOrchid', 'DeepSkyBlue', 'goldenrod', 'PaleGreen')[random.randint(0, 4)])
    turtle.dot()
    for i in range(8):
      turtle.speed(15)
      for _ in range(3):
        turtle.forward(size)
        turtle.left(45)
        turtle.forward(size)
        turtle.backward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(45)
      turtle.forward(size)
      turtle.backward(size * 4)
      turtle.left(45)

snowflake()