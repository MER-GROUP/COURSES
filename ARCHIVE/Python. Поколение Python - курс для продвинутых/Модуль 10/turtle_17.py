import turtle as t
		
def luch(n, size):
	t.shape('classic')
	for i in range(n):
		t.forward(size)
		t.stamp()
		t.backward(size)
		t.left(360 / n)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('circle')
	t.speed(10)
	t.stamp()
	luch(8, 100)
	t.hideturtle()
	t.done()