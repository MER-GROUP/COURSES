'''
Напишите программу, которая рисует изображение по образцу. 
Звезды должны быть рассыпаны случайно, иметь разный размер и цвет.
'''

'''
Угол каждой вершины пятиконечной звезды составляет - 36°. 
Это школьная теорема. Если в многоугольнике нечётное количество сторон, 
то соотношение угла между соседними вершинами к углу самих вершин звёзд равно 3. 
Так получаем: 180* (5-2) - все углы пятиугольника, 540/5 - один угол, 
и 540/15=36. Ну или легко доказать так: 1) в центре звёзды 
правильный пятиугольник, т.к. он вписан в правильный пятиугольник с помощью диагоналей.
'''
import turtle as t

def check(obj):
	try:
		obj.Screen()
		obj.colormode()
		return True
	except (AttributeError):
		return False

def settings(obj, bgcolor, pencolor):
	if check(obj):
		obj.Screen().bgcolor(bgcolor)
		obj.colormode(255)
	obj.pencolor(pencolor)
	obj.showturtle()
	obj.shape('classic')
	obj.speed(0)
	obj.hideturtle()

def speed(obj):
	try:
		obj.tracer(8)
	except (AttributeError):
		obj._tracer(8)

def goto(x, y, obj):
	obj.penup()
	obj.goto(x, y)
	obj.pendown()
	
def circle(r, color, obj):
	obj.fillcolor(color)
	obj.begin_fill()
	obj.circle(r)
	obj.end_fill()

def star(length, angle, obj, bgcolor, pencolor):
	obj.left(angle)
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	for i in range(10):
		if 0 == i % 2:
			obj.forward(length)
			obj.left(72)
		else:
			obj.forward(length)
			obj.right(144)
	obj.end_fill()
	obj.pencolor('black')
	
if __name__ == '__main__':
	# settings turtle
	settings(t, 'white', 'black')
	speed(t)

	# algorithm
	# goto(320, 240, t)
	from random import randint as r
	for _ in range(100):
		x = r(-320, 320)
		y = r(-240, 240)
		goto(x, y, t)
		angle = r(0, 360)
		length = r(5, 20)
		color = (r(0, 255), r(0, 255), r(0, 255))
		star(length, angle, t, color, color)

	t.done()