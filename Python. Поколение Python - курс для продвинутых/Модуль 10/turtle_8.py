import turtle as t

def hexagon(side):
	for i in range(4):
		t.forward(side)
		if 0 == i % 2:
			t.left(120)
		else:
			t.left(60)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	hexagon(100)
	t.hideturtle()
	t.done()