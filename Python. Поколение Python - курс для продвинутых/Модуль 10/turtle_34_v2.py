'''
Создал одну черепашку для луны и две для тени. 
Луну оставил на месте, нарисовал точку (200). 
Тени по очереди - одной рисую точку, 
затем другую стираю и перемещаю на новое место - на 2 точки влево, 
цикл от 145 до -145 (подобрал, сам не понял, почему). 
Всё в бесконечном цикле While True. 
За счёт двух чередующихся теней обеспечена плавность перемещения.
'''
import turtle as t
t.colormode(255)

moon = t.Turtle()
moon.color(230,150,0)

sh1 = t.Turtle()
sh1.color('blue')
sh2 = t.Turtle()
sh2.color('blue')
l = (sh1, sh2)
moon.pu()
moon.ht()
sh1.pu()
sh1.ht()
sh2.pu()
sh2.ht()
t.Screen().bgcolor('blue')
moon.dot(200)
while True:
    for x in range(144, -144, -1):
        l[(x + 1) % 2].dot(200)
        l[x % 2].clear()
        l[x % 2].setx(x)