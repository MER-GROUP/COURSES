import turtle as t, math

t.Screen().bgcolor('black')
colors = ['#ffff66','#ad5a00','#fd5a0A', 'cyan',
'#FF6347','#ad5a00','#ad5a00','#20B2AA', '#4169E1','#ad5a00']
f = ('Times New Roman', 11, 'normal')
lst = [[(-150, 0), (-170, -20)], [(-80, 80), (-100, 60)],
[(-40, 20), (-60, 5)], [(-80, -100), (-100, -120)], [(0, -120), (-10, -135)],
[(60, 60), (40, 40)], [(110, -100), (90, -120)]]

circ = [50, 10, 20, 15, 12, 40, 45]
plan = ['Солнце', 'Меркурий', 'Венера', 'Эемля', 'Марс', 'Юпитер', 'Сатурн']
i = 0
t.up()
for a, b in lst:
  t.goto(a)
  t.fillcolor(colors[i])
  t.begin_fill()
  t.circle(circ[i])
  t.end_fill()
  t.goto(b)
  t.fillcolor('white')
  t.write(plan[i], font=f)
  i += 1

t.goto(110, -85)
t.pensize(5)
t.down()
t.pencolor('blue')
a, b = 70, 30
dx = t.xcor()
dy = t.ycor()
for deg in range(361):
    rad = math.radians(deg)
    x = a * math.sin(rad) + dx
    y = -b * math.cos(rad) + b + dy
    t.goto(x, y)

t.done()