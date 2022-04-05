import turtle as t

def rectangle(width, height):
  for i in range(4):
    t.right(90)
    t.forward(height) if i % 2 == 0 else t.forward(width)


t.showturtle()
t.shape("classic")
w, h = 180, 100
rectangle(w, h)
t.hideturtle()
t.done()