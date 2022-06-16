import turtle as T
import random as R
# Функция построения здания
def building(width, height):
    T.fillcolor('darkblue')
    T.begin_fill()
    for i in range(4):
        T.forward((width, height)[i%2])
        T.left(90)
    T.end_fill()

# Функция размещения звёзд
def stars(W, H, n):
    for _ in range(n):
        T.goto(R.randint(-W/2, W/2), R.randint(-H/2, H/2))
        T.dot(R.randint(2, 4), 'yellow')

# Функция размещения окон
def windows(w, h, n):
    T.color('yellow')
    x, y = int(T.xcor() + 15), int(T.ycor() + 15)
    for _ in range(n):
        T.goto(R.randrange(x, x + w, 30), R.randrange(y, y + h, 30))
        T.stamp()
# --- --- ---
W, H = 600, 600
w_available = W
T.Screen().setup(W, H), T.bgcolor('midnightblue'), T.shape('square'), T.speed(0), T.penup()
# --- --- ---
stars(W, H, 50)
T.goto(-W/2, -H/2)
while w_available > 0:
    w, h = R.randrange(60, 151, 30), R.randrange(180, H - 50, 30)
    building(w, h)
    windows(w, h, R.randrange(1, 8))
    w_available -= w
    T.goto(W / 2 - w_available, -H / 2)
T.done()