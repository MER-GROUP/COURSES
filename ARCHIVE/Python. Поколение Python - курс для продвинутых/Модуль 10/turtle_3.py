import turtle as t

def triangle(side):
	for _ in range(3):
		t.forward(side)
		t.left(120)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	triangle(300)
	t.hideturtle()
	t.done()