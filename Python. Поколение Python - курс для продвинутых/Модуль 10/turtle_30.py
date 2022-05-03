import turtle as t

def goto_over(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	
def square(size1, size2):
	t.fillcolor('black')
	t.begin_fill()
	for i in range(4):
		_size = [size1, size2][i % 2]
		t.forward(_size)
		t.left(90)
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
	goto_over(-75, -200)
	square(150, 400)
	goto_over(t.xcor() + 75, t.ycor() + 30)
	circle(50, 'lightgreen')
	goto_over(t.xcor(), t.ycor() + 120)
	circle(50, 'yellow')
	goto_over(t.xcor(), t.ycor() + 120)
	circle(50, 'red')
	t.hideturtle()
	t.done()