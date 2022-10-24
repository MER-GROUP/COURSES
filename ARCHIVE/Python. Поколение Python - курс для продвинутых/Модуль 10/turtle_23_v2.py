'''
Нарисовано не поднимая перо,  2 цикла - вначале шестиугольник, затем все остальное
'''
import turtle

for i in range(6):
  turtle.left(360 / 6)
  turtle.forward(80)
for i in range(12):
  turtle.forward(80)
  turtle.left(120 + 180 * (i % 2))
  
turtle.done()