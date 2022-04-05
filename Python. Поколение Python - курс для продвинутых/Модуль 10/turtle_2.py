import turtle as t

def rectangle(width, height):
	for _ in range(2):
		t.forward(width)
		t.left(90)
		t.forward(height)
		t.left(90)
	
t.showturtle()
rectangle(100, 200)