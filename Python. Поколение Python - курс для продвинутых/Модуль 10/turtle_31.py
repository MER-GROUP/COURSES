import turtle as t

def goto_over(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	
def triangle(size, color, direct):
	t.pencolor(color)
	t.fillcolor('white')
	t.begin_fill()
	for i in range(3):
		_size = size
		t.forward(_size)
		if 'left' == direct: t.left(120)
		else: t.right(120)
	t.end_fill()
	
def circle(r, color):
	t.fillcolor(color)
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(0)
	goto_over(-150, -150)
	triangle(300, 'black', 'left')
	goto_over(t.xcor(), t.ycor() + 110)
	circle(50, 'black')
	goto_over(t.xcor() + 300, t.ycor())
	circle(50, 'black')
	goto_over(t.xcor() - 150, t.ycor() - 235)
	circle(50, 'black')
	goto_over(t.xcor() - 150, t.ycor() + 300)
	triangle(300, 'white', 'right')
	t.hideturtle()
	t.done()