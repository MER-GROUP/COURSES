import turtle as T

q = ["Север", "Восток", "Юг", "Запад"]
T.circle(40)
T.left(90)
T.forward(40)
for i in range(4):
    T.forward(80)
    T.penup()
    T.forward(30)
    T.write(q[i], align="center")
    T.back(110)
    T.right(90)
    T.pendown()
T.done()