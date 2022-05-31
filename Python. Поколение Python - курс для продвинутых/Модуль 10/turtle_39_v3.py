import turtle as t 

def draw_ellipse(rad):  # Функция рисует эллипс
    for i in range(2):
        t.circle(rad - 45, 90)
        t.circle(rad // 2 - 45, 90)

def draw_planet(planet, r, color, x):
  t.speed(0)
  t.fillcolor(color)
  t.penup()
  t.goto(x, 0)
  t.right(90)
  t.forward(r)
  t.left(90)
  t.pendown()
  t.begin_fill()
  t.circle(r)
  t.end_fill()
  t.fillcolor('white')
  t.penup()
  t.right(90)
  t.forward(20)
  t.left(90)
  t.write(*planet)
  
t.Screen().setup(1000, 400) 
t.Screen().bgcolor('black')
planets = [('Солнце', False, 'center', ('Arial', 10, 'normal')), 
           ('Меркурий', False, 'center', ('Arial', 10, 'normal')),
           ('Венера', False, 'center', ('Arial', 10, 'normal')),
           ('Земля', False, 'center', ('Arial', 10, 'normal')),
           ('Марс', False, 'center', ('Arial', 10, 'normal')), 
           ('Юпитер', False, 'center', ('Arial', 10, 'normal')),
           ('Сатурн', False, 'center', ('Arial', 10, 'normal')),
           ('Уран', False, 'center', ('Arial', 10, 'normal')),
           ('Нептун', False, 'center', ('Arial', 10, 'normal')),
           ('Плутон', False, 'center', ('Arial', 10, 'normal'))] 
           
colors = ['yellow', 'orange', 'orange', 'lightgreen', 'darkred', 'orange', 'orange', 'lightblue', 'blue', 'orange']
radius = [600, 8, 20, 15, 10, 60, 50, 30, 25, 5]
x_position = [-1050, -380, -300, -225,  -150, -50, 80, 180, 260, 320]

for i in range(10):
  planet = planets[i]
  color = colors[i]
  r = radius[i]
  x = x_position[i]
  draw_planet(planet, r, color, x)
  
  if i == 6:  # Если Сатурн, то добавляет кольцо
    t.penup()
    t.goto(x - r//2, -r)
    t.pendown()
    t.pencolor('white')
    draw_ellipse(130)

t.done()