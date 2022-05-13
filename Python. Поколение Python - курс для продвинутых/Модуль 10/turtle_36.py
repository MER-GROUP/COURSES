'''
Напишите программу, которая рисует изображение 
правильных многоугольников по образцу. 
Многоугольники должны иметь разный цвет.

Примечание 1. Доработайте программу, 
чтобы площадь всех многоугольников была одинаковой.

Примечание 2. Обратите внимание на то, что тригонометрические 
функции модуля math работают с радианами, а не градусами. 
Для преобразования градусов в радианы используйте функцию radians.
'''

'''
Правильный многоугольник это многоугольник с равными сторонами и 
равными углами. Например, каждый угол равностороннего треугольника 
вычисляется так: 180 ÷ 3 = 60°, а каждый угол квадрата находится 
так: 360 ÷ 4 = 90°. Вычтите сумму всех известных углов из общей 
суммы углов неправильного многоугольника. Если стороны многоугольника 
не равны друг другу, и его углы также не равны друг другу, 
сначала сложите известные углы многоугольника.
'''
import turtle as t
import math as m

class MyExeption(BaseException):
	pass

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

def polygon(length, count_sides, obj, bgcolor, pencolor):
	length = length
	count_sides = count_sides
	try:
		if 3 > count_sides:
			raise MyExeption
	except (MyExeption):
		count_sides = 3
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	angle_sum = (count_sides - 2) * 180
	angle = 180 - angle_sum / count_sides
	for _ in range(count_sides):
		obj.forward(length)
		obj.right(angle)
	obj.end_fill()
	obj.pencolor('black')
	# test
	# print('length =', length)
	# s = square_polygon(length, count_sides)
	# len_side_polygon(s, count_sides)

def square_polygon(length, count_sides):
	s = round((count_sides * length ** 2) / (4 * m.tan(m.radians(180 / count_sides)))) 
	# test
	# print('s =', s)
	return s

def len_side_polygon(s, count_sides):
	length = round(m.sqrt((s * 4 * m.tan(m.radians(180 / count_sides))) / count_sides))
	# test
	# print('length =', length)
	return length

	
if __name__ == '__main__':
	# settings turtle
	settings(t, 'white', 'black')
	speed(t)

	# algorithm
	# polygon(50, 9, t, 'red', 'green')
	length = int()
	for count in range(3, 15):
		goto(-300, -200)

	t.done()