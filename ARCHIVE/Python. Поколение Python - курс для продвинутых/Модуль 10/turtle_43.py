'''
Напишите программу, которая по нажатию на левую кнопку мыши рисует звезду в месте клика. 
Фон изображения должен быть черным, при этом звезды могут иметь разные размеры, 
цвета и иметь разное количество сторон.
'''
import turtle as t
import math as m
import random as r

class MyExeption(Exception):
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
	
def circle(r, bgcolor, pencolor, obj):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	obj.circle(r)
	obj.end_fill()
	obj.pencolor('black')

def oval(r, bgcolor, pencolor, obj):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	obj.right(45)
	for _ in range(2):
		obj.circle(r, 90)
		obj.circle(r / 2, 90)
	obj.end_fill()
	obj.pencolor('black')

def oval_line(r, obj):
	a = r + int(r / 2)
	b = r - int(r / 4)
	dx = obj.xcor()
	dy = obj.ycor()
	for deg in range(361):
		rad = m.radians(deg)
		x = a * m.sin(rad) + dx
		y = -b * m.cos(rad) + b + dy
		obj.goto(x, y)

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

def box(length, bgcolor, pencolor, obj):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	for i in range(4):
		obj.forward(length)
		obj.right(90)
	obj.end_fill()
	obj.pencolor('black')

def cross(side, pencolor, obj):
	obj.pencolor(pencolor)
	for _ in range(4):
		obj.forward(side)
		goto(0, 0, obj)
		obj.left(90)

def text(*arr, obj, side):
	font_size = 15
	font_size_part = font_size - 10
	side_part = side // 10
	goto(-side - side_part, -font_size + font_size_part, obj)
	obj.write(arr[0], move=False, align='right', font=('Time New Roman', font_size, 'normal'))
	goto(0, -side - side_part * 2, obj)
	obj.write(arr[1], move=False, align='center', font=('Time New Roman', font_size, 'normal'))
	goto(side + side_part, -font_size + font_size_part, obj)
	obj.write(arr[2], move=False, align='left', font=('Time New Roman', font_size, 'normal'))
	goto(0, side + side_part, obj)
	obj.write(arr[3], move=False, align='center', font=('Time New Roman', font_size, 'normal'))

def rectangle(a, b, bgcolor, pencolor, obj):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	for i in range(4):
		obj.forward([a, b][i % 2])
		obj.left(90)
	obj.end_fill()
	obj.pencolor('black')

def heart(obj, bgcolor, pencolor):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	for deg in range(360):
		rad = m.radians(deg)
		x = 128*m.sin(rad)**3
		y = 8*(13*m.cos(rad)-5*m.cos(2*rad)-2*m.cos(3*rad)-m.cos(4*rad) - 5)
		obj.goto(x, y)
	obj.end_fill()
	obj.pencolor('black')

def random_color():
	return r.randrange(256), r.randrange(256), r.randrange(256) 

def random_length():
	return r.randint(1, 20)

def random_angle():
	return r.randrange(360)

def draw_circle(x, y, r):
	t.penup()
	t.goto(x, y - r)
	t.pendown()
	color = random_color()
	t.pencolor(color)
	t.fillcolor(color)
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	t.speed(0)

def left_mouse_click(x, y):
	draw_circle(x, y, 10)

def draw_star(pencolor, bgcolor, obj):
	length = random_length()
	angle = random_angle()	
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

def draw_poly_star(pencolor, bgcolor, obj):
	import random as ra
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	obj.left(ra.randrange(360))
	R, r = ra.randint(30, 70), ra.randint(5, 20)
	x = int(obj.xcor())
	y = int(obj.ycor())
	pi = m.pi
	i = 1
	n = ra.randint(3, 10)
	while (i<=n*2):
		goto(x+m.cos(i*pi/n)*r, y+m.sin(i*pi/n)*r, obj)
		i=i+1
		goto(x+m.cos(i*pi/n)*R, y+m.sin(i*pi/n)*R, obj)
		i=i+1
	goto(x+m.cos(i*pi/n)*r, y+m.sin(i*pi/n)*r, obj)
	i=i+1
	obj.end_fill()
	obj.pencolor('black')

def left_mouse_click_for_star(x, y):
	goto(x, y, t)
	color = random_color()
	# draw_star(color, color, t)
	draw_poly_star(color, color, t)

if __name__ == '__main__':
	# settings turtle
	# settings(t, 'white', 'black')
	settings(t, 'black', 'white')
	speed(t)

	# over set
	# t.Screen().bgcolor('white')
	# set screen size
	t.Screen().setup(640, 480)

	# var
	pass

	# algorithm
	t.Screen().onclick(left_mouse_click_for_star)
	t.Screen().listen()

	# pause
	t.done()