import turtle as t
		
def luch(n, size1, size2, size3):
	for i in range(n):
		t.forward(size1)
		t.pendown()
		t.forward(size2)
		t.penup()
		t.forward(size3)
		t.stamp()
		t.backward(size1 + size2 + size3)
		t.left(360 / n)
	
if __name__ == '__main__':
	t.Screen().bgcolor('lightblue')
	t.showturtle()
	t.shape('turtle')
	t.speed(10)
	t.pensize(5)
	t.penup()
	t.stamp()
	luch(12, 70, 10, 20)
	t.hideturtle()
	t.done()