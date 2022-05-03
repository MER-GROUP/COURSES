from turtle import *

side = 200
r = 3 ** 0.5 * side / 6
hideturtle()

# Устанавливаем начальную точку, с которой начнем рисовать
up()
goto(-r * 2, -r)
down()

# Рисуем 1-й треугольник
for i in range(3):
  forward(side)
  left(120)
  
# Рисуем 2-й треугольник и три круга
up()
goto(-r * 2, r)
down()
fillcolor('white')
begin_fill()
for i in range(3):
  dot(r)
  pencolor('white')
  forward(side)
  pencolor('black')
  right(120)
end_fill()