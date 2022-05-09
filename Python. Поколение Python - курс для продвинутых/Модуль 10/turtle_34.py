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
	
if __name__ == '__main__':
	# global var
	color = ('orange', 'blue')

	# settings
	print('main type(t)', type(t))
	settings(t, color[1], color[1])

	# moon settings
	moon = t.Turtle()
	settings(moon, color[0], color[0])
	goto(moon.xcor(), moon.ycor() - 150, moon)
	circle(150, color[0], moon)

	# shadow settings
	shadow = t.Turtle()
	settings(shadow, color[1], color[1])
	goto(shadow.xcor() + 300, shadow.ycor() - 150, shadow)
	circle(150, color[1], shadow)

	# shadow2 settings
	shadow2 = t.Turtle()
	settings(shadow2, color[1], color[1])
	goto(shadow2.xcor() + 300, shadow2.ycor() - 150, shadow2)

	# test shadow.xcor
	# print(shadow.xcor())

	# animation
	shadow._tracer(8, 0) # speed animation
	while True:
		goto(shadow.xcor()-1, shadow.ycor(), shadow)
		goto(shadow2.xcor()-1, shadow2.ycor(), shadow2)
		circle(150, color[1], shadow)
		circle(150, color[1], shadow2)
		if 0 == int(shadow.xcor() + 1) % 2:
			shadow.clear()
		else:
			shadow2.clear()
		if (-300 == int(shadow.xcor())):
			shadow.setx(300)
			shadow2.setx(300)
		# print(shadow.xcor())

	t.done()