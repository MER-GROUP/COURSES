import turtle as t

def triangle(size, direction):
	angle = 120 if 'right' == direction else (180 + 60)
	for _ in range(3):
		t.forward(size)
		t.right(angle)
	
t.showturtle()
t.shape('classic')
t.speed(10)
t.penup()
t.goto(-50, 50)
t.pendown()
triangle(100, 'right')
t.penup()
t.goto(-50, -10)
t.pendown()
triangle(100, 'left')

t.hideturtle()
t.done()