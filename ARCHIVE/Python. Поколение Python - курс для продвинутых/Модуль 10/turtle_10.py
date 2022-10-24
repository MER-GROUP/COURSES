import turtle as t

def hexagon(side):
	for _ in range(12):
		t.forward(side)
		t.backward(side)
		t.left(30)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	hexagon(100)
	t.hideturtle()
	t.done()