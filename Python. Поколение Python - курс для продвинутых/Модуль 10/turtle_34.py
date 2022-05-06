import turtle as t

def goto_over(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	
def circle(r, color):
	t.fillcolor(color)
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	
if __name__ == '__main__':
	t.Screen().bgcolor('blue')
	t.pencolor('blue')
	t.showturtle()
	t.shape('classic')
	t.speed(0)
	color = ('orange', 'blue')
	t.left(90)
	r1 = 150
	r2 = 150
	d = 5
	x = 150
	y = 0
	goto_over(t.xcor() + x, t.ycor() + y)
	circle(r1, color[0])
	x = 300
	goto_over(t.xcor() + x, t.ycor() + y)
	circle(r2, color[1])
	while True:
		goto_over(t.xcor() - d, t.ycor())
		circle(r2, color[1])
		print(int(t.xcor()))
		if (150 == int(t.xcor())):
			break
	goto_over(0, 0)
	x = 150
	goto_over(t.xcor() + x, t.ycor() + y)
	circle(r1, color[0])
	x2 = 150
	xd = 150
	# новое перо (второй верхний слой)
	t2 = t.Turtle()
	while True:
		print(xd)
		if (-120 == int(t.xcor())):
			break
		xd -= d
		goto_over(xd, t.ycor())
		circle(r2, color[1])

	t.hideturtle()
	t.done()