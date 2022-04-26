import turtle as t

def uzor(size_n, line, ugol):
		angle = ugol
		t.forward(size_n)
		t.left(angle)
		t.forward(line)
		t.backward(line)
		t.right(angle * 2)
		t.forward(line)
		t.backward(line)
		t.left(angle)
		
def luch(n, size, color):
	t.pencolor(color)
	size_n = size / 3
	line = size_n - (size_n / 5)
	for i in range(n):
		uzor(size_n, line, 50)
		uzor(size_n, line, 50)
		uzor(size_n, line, 50)
		t.forward(size_n)
		t.backward(size + size_n)
		t.left(360 / n)
	
if __name__ == '__main__':
	t.Screen().bgcolor('aqua')
	t.showturtle()
	t.shape('classic')
	t.speed(0)
	t.pensize(3)
	luch(8, 60, 'magenta')
	t.penup()
	t.goto(200, 200)
	t.pendown()
	luch(8, 100, 'gray')
	t.penup()
	t.goto(-200, 200)
	t.pendown()
	luch(8, 40, 'purple')
	t.penup()
	t.goto(-200, -200)
	t.pendown()
	luch(8, 80, 'blue')
	t.penup()
	t.goto(200, -200)
	t.pendown()
	luch(8, 100, 'indigo')
	t.hideturtle()
	t.done()