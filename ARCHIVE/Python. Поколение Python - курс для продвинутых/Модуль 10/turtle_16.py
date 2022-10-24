import turtle as t

def box(a, b):
	for i in range(4):
		t.dot()
		size = a if not i % 2 else b
		t.forward(size)
		t.left(90)
		
def box_stamp(a, b):
	t.shape('circle')
	for i in range(4):
		t.stamp()
		size = a if not i % 2 else b
		t.forward(size)
		t.right(90)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	box(100, 50)
	t.pu()
	t.rt(90)
	t.fd(50)
	t.lt(90)
	t.pd()
	box_stamp(100, 50)
	t.hideturtle()
	t.done()