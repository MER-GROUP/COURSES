import turtle as t

def goto_over(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
		
def triandle(size):
	t.fillcolor('saddlebrown')
	t.begin_fill()
	for i in range(3):
		angle = [129, 102][i % 2]
		_size = size if 0 == i else size - size / 5
		t.forward(_size)
		t.left(angle)
	t.end_fill()
	
def square(size):
	t.fillcolor('dodgerblue')
	t.begin_fill()
	for i in range(4):
		_size = [size, size - size / 5][i % 2]
		t.forward(_size)
		t.right(90)
	t.end_fill()
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	goto_over(-200/2, 0)
	triandle(200)
	goto_over(t.xcor() + 20, 0)
	square(160)
	t.hideturtle()
	t.done()