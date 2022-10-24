import turtle

# Функция рисования 1 квадрата
def square(size_square, color_square):
  turtle.pendown()
  turtle.fillcolor(color_square)
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(size)
    turtle.right(90)
  turtle.end_fill()
  
screen = 500    # Параметр размера графического окна
squares = 5     # Размерность поля (5х5 квадратов)
size = screen / (2 * squares)   # размер стороныквадрата
turtle.Screen().setup(screen, screen)
colors = ('black', 'white')   # Кортеж цветов

turtle.speed(0)
turtle.hideturtle()
x = -size * squares / 2     # Начальная координата поля Х
y = size * squares / 2      # Начальная координата поля Y
for i in range(squares):
  y -= size * (i != 0)      # Установка начальной координаты
  x = -size * squares / 2   # для каждой строки
  for j in range(squares):
    x += size * (j != 0)    # Изменение координаты Х для каждого квадрата
    turtle.penup()
    turtle.goto(x, y)
    square(size, colors[(i + j) % 2])

turtle.done()