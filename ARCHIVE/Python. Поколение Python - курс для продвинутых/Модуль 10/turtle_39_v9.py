from turtle import *

def kolco(r):
    pendown()
    right(45)
    for loop in range(2):
        circle(r, 90)
        circle(r / 2, 90)

speed(0)
penup()
ht()

names = ['Солнце', 'Меркурий', 'Венера', 'Земля', 'Марс',
    'Юпитер', 'Сатурн', 'Уран', 'Нептун', 'Плутон']
coordinates1 = [(-380, -80), (-265, -10), (-215, -16), (-165, -17),
                 (-125, -12), (-45, -50), (90, -60), (200, -35), (280, -32), (340, -7)]
coordinates2 = [(-380, -100), (-265, -35), (-215, -35),
                 (-165, -35), (-125, -35), (-45, -70), (90, -75), (200, -55), (280, -55), (340, -55)]
colors = ['LightGoldenRod1', 'khaki3', 'CadetBlue1', 'LawnGreen',
    'firebrick', 'DarkGoldenRod', 'PaleGoldenrod', 'moccasin', 'DeepSkyBlue', 'DarkSalmon']
radius = (80, 10, 16, 17, 12, 50, 60, 35, 32, 7)

for i in range(len(names)):
    goto(coordinates1[i])
    pendown()
    begin_fill()
    fillcolor(colors[i])
    circle(radius[i])
    end_fill()
    penup()
    goto(coordinates2[i])
    write(names[i], align='center')

goto(34, -26)
kolco(80)
done()