'''
Напишите программу, которая рисует силуэты многоэтажек по образцу. 
Разделите программу на функции:

рисования контуров зданий;
рисования нескольких окон в зданиях;
рисования случайно разбросанных звезд в виде точек 
(убедитесь, что звезды появляются на небе, а не на зданиях).
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

if __name__ == '__main__':
	# settings turtle
	settings(t, 'white', 'black')
	speed(t)

	# over set
	t.Screen().bgcolor('MidnightBlue')
	# set screen size
	# t.Screen().setup(640, 480)
	t.Screen().setup(645, 495)

	# var
	pass

	# algorithm
	# draw stars
	for _ in range(100):
		x = r.randint(-320, 320)
		y = r.randint(-240, 240)
		goto(x, y, t)
		radius = r.randint(1, 3)
		circle(radius, 'yellow', 'yellow', t)
	# draw rectangle
	goto(-320, -240, t)
	h_min = 200
	h_max = 400
	w_min = 50
	w_max = 150
	w_general = 0
	w_setup = 640
	while True:
		w = r.randint(w_min, w_max)
		w_back = w_general
		w_general += w
		h = r.randint(h_min, h_max)
		if w_setup >= w_general:
			# draw houses
			rectangle(w, h, 'MediumBlue', 'MediumBlue', t)
			# save coords
			x = int(t.xcor()) + w
			y = int(t.ycor())
			# draw windows
			step2_x = 5
			step2_y = 15
			x2 = x - w
			x2_begin = x2
			y2 = y
			x2_end = x
			y2_end = y + h
			while True:
				x2 += step2_x
				goto(x2, y2, t)
				if (r.randint(0, 1)):
					rectangle(10, 10, 'yellow', 'yellow', t)
					x2 += 10
				else:
					x2 += 10				
				if x2 + step2_x + 10>= x2_end:
					x2 = x2_begin
					y2 += step2_y
				if y2 + step2_y >= y2_end:
					break
			goto(x, y,t)
		else:
			# w_end = w_general - w_setup
			w_end = w_setup - w_back
			rectangle(w_end, h, 'MediumBlue', 'MediumBlue', t)
			# save coords
			# x = int(t.xcor()) + w
			x = int(t.xcor()) + w_end
			y = int(t.ycor())
			# draw windows
			step2_x = 5
			step2_y = 15
			# x2 = x - w
			x2 = x - w_end
			x2_begin = x2
			y2 = y
			x2_end = x
			y2_end = y + h
			while True:
				x2 += step2_x
				goto(x2, y2, t)
				if (r.randint(0, 1)):
					rectangle(10, 10, 'yellow', 'yellow', t)
					x2 += 10
				else:
					x2 += 10				
				if x2 + step2_x + 10>= x2_end:
					x2 = x2_begin
					y2 += step2_y
				if y2 + step2_y >= y2_end:
					break
			break


	# pause
	t.done()