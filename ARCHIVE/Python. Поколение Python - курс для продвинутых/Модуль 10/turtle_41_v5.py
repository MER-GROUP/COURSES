import turtle as t
import random as r

t.Screen().setup(480, 480)
t.Screen().colormode(255)
t.speed(10)

def buildings(width, height):   # рисуем одно здание
    t.fillcolor(65, 99, 192)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    
def stars():   # рисуем звезды
    for i in range(50):
        t.pencolor(255, 255, 153)
        t.dot(r.randint(1, 6))
        t.goto(r.randint(-240, 240), r.randint(-70, 240))
        
def window(x, y):  # рисуем окно
    t.goto(x, y)
    t.fillcolor(255, 255, 153)
    t.begin_fill()
    for i in range(4):
      t.forward(15)
      t.left(90)
    t.end_fill()
    
# основная часть
t.Screen().bgcolor(13, 36, 102)
build_size = [(60, 160), (80, 230), (110, 400), (60, 200), (80, 320), (40, 230), (50, 160)]
build_width = [i[0] for i in build_size]
wind_koord = [(-170, -40), (-90, 130), (-90, 110), (-10, 55), (-50, -60), (80, 30)]

t.penup()
stars()
t.goto(-240, -240) 
for i in range(len(build_size)):
      buildings(build_size[i][0], build_size[i][1])
      t.goto(-240 + sum(build_width[:i + 1]), -240)
      t.left(90)

for i in range(6):
    window(wind_koord[i][0], wind_koord[i][1])

t.done()