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

def goto(x, y, obj):
	obj.penup()
	obj.goto(x, y)
	obj.pendown()
	
def circle(r, color, obj):
	obj.fillcolor(color)
	obj.begin_fill()
	obj.circle(r)
	obj.end_fill()

def star(length, obj, color):
	angle = 0
	t.fillcolor(color)
	t.begin_fill()
	for i in range(10):
		t.forward(length)
		t.right(144)
	t.end_fill()
	
if __name__ == '__main__':
	# settings turtle
	print('main type(t)', type(t))
	settings(t, 'white', 'black')

	# algorithm
	star(100, t, 'red')

	pass

	t.done()