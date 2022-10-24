import turtle as t
		
def luch(n, size):
	for i in range(n):
		t.forward(size)
		t.stamp()
		t.backward(size)
		t.left(360 / n)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('turtle')
	t.speed(10)
	t.penup()
	t.stamp()
	luch(10, 100)
	t.hideturtle()
	t.done()