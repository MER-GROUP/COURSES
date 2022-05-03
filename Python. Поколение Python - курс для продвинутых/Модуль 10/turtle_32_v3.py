import turtle

color = ['red', 'orange', 'yellow', 'LimeGreen', 'MediumSeaGreen', 'cyan', 'blue', 
'DarkBlue', 'VioletRed', 'DeepPink']
color.reverse()

for i in range(100, 0, -10):
  turtle.penup()
  turtle.goto(0, -i+10)
  turtle.pendown()
  turtle.begin_fill()
  turtle.fillcolor(color[i//10-1])
  turtle.circle(i)
  turtle.end_fill()
  
turtle.ht()