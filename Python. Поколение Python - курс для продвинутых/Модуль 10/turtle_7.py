import turtle as t

def hexagon(side):
	for _ in range(6):
		for _ in range(6):
			t.forward(side)
			t.left(60)
		t.left(120)
		t.forward(side)
		t.right(60)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	hexagon(100)
	t.hideturtle()
	t.done()