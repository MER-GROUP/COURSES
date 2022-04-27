# Вывод текста в графическое окно
# Для вывода текста в графическое окно применяется команда write(). Аргумент этой команды — строка текста, которую требуется вывести на экран. Левый нижний угол первого символа выведенного текста будет расположен в точке с координатами черепашки.
import turtle
turtle.write('Пpивeт, мир!')
# выводит текст Привет, мир! на экран.

# Приведенный ниже код показывает, как черепаха перемещается в соответствующие позиции для вывода текста:
import turtle
turtle.Screen().setup(400, 300)
turtle.hideturtle()
turtle.goto(-120, 120)
turtle.write('Сверху')
turtle.goto(50, -120)
turtle.write('Снизу')
turtle.goto(100, 20)
turtle.write('Справа')

# Мы можем настроить вывод текста, задавая размер и тип шрифта, начертание, выравнивание и т.д.
'''
Аргументы команды write():

	arg – текст, который нужно вывести;
	move – указывает будет ли двигаться черепашка по мере рисования надписи (по умолчанию значение False);
	align – служит для выравнивания надписи относительно черепашки, может принимать три строковых значения right, center, left (по умолчанию значению right);
	font – кортеж из трех значений: (название шрифта, размер шрифта, тип начертания). В качестве начертания можно использовать строковые значения: normal — обычный, bold — полужирный, italic — курсив, или объединить два последних, тогда текст будет напечатан полужирным курсивом.
'''
import turtle

turtle.hideturtle()
turtle.goto(-120, 120)
turtle.write('Сверху', move=True, align='center', font=('Arial', 17, 'bold'))
turtle.goto(50, -120)
turtle.write('Снизу', move=True, align='left', font=('Times New Roman', 25, 'normal'))
turtle.goto(100, 20)
turtle.write('Справа', move=True, align='right', font=('Helvetica', 20, 'italic'))

# Заполнение геометрических фигур
# Для заполнения геометрической фигуры цветом используется команда turtle.begin_fill(), причем она применяется до начертания фигуры, а после завершения начертания используется команда turtle.end_fill() и геометрическая фигура заполняется текущим цветом заливки.
# Приведенный ниже код:
import turtle
# спрятать черепашку
turtle.hideturtle()
# # включаем заливку
turtle.begin_fill()
turtle.circle(80)
# выключаем заливку
turtle.end_fill()
# рисует круг, заполненный цветом по умолчанию — черным.

# Цвет заливки можно изменить при помощи команды fillcolor(). Аргумент команды — название цвета в виде строкового литерала, либо значения трех компонентов RGB.
# Приведенный ниже код:
import turtle
turtle.hideturtle()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
# изменяет цвет рисунка на красный и рисует круг.

# Приведенный ниже код:
# рисует квадрат, заполненный зеленым цветом.
import turtle
turtle.hideturtle()
turtle.fillcolor('green')

turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

# Если заполнить незамкнутую фигуру, она будет закрашена, будто был начерчен отрезок, соединяющий начальную и конечную точки.
# Приведенный ниже код:
# рисует зеленый четырехугольник.
import turtle
turtle.hideturtle()
turtle.fillcolor('green')

turtle.begin_fill()
turtle.goto(-50, 120)
turtle.goto(120, 120)
turtle.goto(150, -80)
turtle.end_fill()

# Создание нескольких черепашек
# Можно работать сразу с несколькими черепашками. Для этого надо создать несколько переменных, содержащих экземпляры класса Turtle.
import turtle
#  устанавливаем цвет фона
turtle.Screen().bgcolor('yellow')
# создаем первую черепашку и устанавливаем ее свойства
tim = turtle.Turtle()
tim.color('red')
tim.pensize(3)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.forward(80)
tim.left(120)
tim.right(180)
tim.forward(80)
# создаем вторую черепашку и устанавливаем ее свойства
alex = turtle.Turtle()
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

# Черепашек можно сохранить в списке, а затем в цикле обрабатывать его.
import turtle
from random import randrange
turtle.Screen().colormode(255)

def move_turtles(turtles, dist, angle):
    # все черепашки из списка делают одни и те же действия
    for turtle in turtles:
        turtle.forward(dist)
        turtle.right(angle)

# список черепашек
turtles = []
head = 0
# количество череашек
num_turtles = 10
for i in range(num_turtles):
    # создаем черепашку и устанавливаем ее свойства
    turt = turtle.Turtle()
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(5)
    turt._tracer(25, 0)
    # добавляем черепашку в список
    turtles.append(turt)
    head = head + 360/num_turtles

for i in range(70):
    move_turtles(turtles, 10, i)
# Команда turtle.tracer(n, delay) включает/выключает анимацию черепашки и устанавливает задержку для обновления рисунков. Может использоваться для ускорения рисования сложной графики.

# Отслеживание нажатия клавиш
# Черепашья графика позволяет отслеживать происходящие события, такие как нажатия клавиш клавиатуры, перемещение мышки или нажатие на мышку. Изначально программа никак не реагирует на эти события и чтобы это поведение изменить необходимо привязать функции обратного вызова к событиям. Для этого существуют специальные команды. Для отслеживания нажатия клавиш клавиатуры используется команда onkey(fun, key), которая связывает функцию обратного вызова fun с событием нажатия клавиши key.
import turtle
# функция обратного вызова
def move_up():
  x, y = turtle.pos()
  turtle.setposition(x, y + 5)
# функция обратного вызова
def move_down():
  x, y = turtle.pos()
  turtle.setposition(x, y - 5)
# функция обратного вызова
def move_left():
  x, y = turtle.pos()
  turtle.setposition(x - 5, y)
# функция обратного вызова
def move_right():
  x, y = turtle.pos()
  turtle.setposition(x + 5, y)
# отображаем черепашку
turtle.showturtle()
# устанавливаем размер пера
turtle.pensize(3)
turtle.shape('turtle')
# устанавливаем фокус на экран черепашки
turtle.Screen().listen()
# регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_up, 'Up')
# регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_down, 'Down') # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_left, 'Left')
# регистрируем функцию на нажатие клавиши направо
turtle.Screen().onkey(move_right, 'Right')
# Для отслеживания событий также необходимо установить фокус на экран черепашки с помощью команды turtle.Screen().listen().

# Давайте теперь сделаем так, чтобы по нажатию на пробел черепашка скрывалась и переставала оставлять след. Также добавим возможность увеличивать скорость перемещения черепашки по нажатию на клавиши клавиатуры q и w.
import turtle
speed = 5
# функция обратного вызова
def move_up():
  x, y = turtle.pos()
  turtle.setposition(x, y + speed)
# функция обратного вызова
def move_down():
  x, y = turtle.pos()
  turtle.setposition(x, y - speed)
# функция обратного вызова
def move_left():
  x, y = turtle.pos()
  turtle.setposition(x - speed, y)
# функция обратного вызова
def move_right():
  x, y = turtle.pos()
  turtle.setposition(x + speed, y)
# функция обратного вызова
def change():
  if turtle.isvisible():
    turtle.up()
    turtle.hideturtle()
  else:
    turtle.down()
    turtle.showturtle()
# функция обратного вызова
def speed_increase():
  global speed
  speed += 1
# функция обратного вызова
def speed_decrease():
  global speed
  speed -= 1
# отображаем черепашку
turtle.showturtle()
# устанавливаем размер пера
turtle.pensize(3)
# устанавливаем фокус на экран черепашки
turtle.Screen().listen()
# регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_up, 'Up')
# регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_down, 'Down') # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_left, 'Left')
# регистрируем функцию на нажатие клавиши направо
turtle.Screen().onkey(move_right, 'Right') 
turtle.Screen().onkey(change, 'space')
turtle.Screen().onkey(speed_increase, 'q')
turtle.Screen().onkey(speed_decrease, 'w')

# Отслеживание нажатия мыши
# Аналогичным образом можно отслеживать нажатие на мышку. Для отслеживания нажатия мыши используется команда onclick(fun), которая связывает функцию обратного вызова fun с событием нажатия левой кнопки мыши.
# Приведенный ниже код рисует круг по нажатию на левую кнопку мыши.
import turtle
from random import randrange
turtle.Screen().colormode(255)

def random_color():
  return randrange(256), randrange(256), randrange(256) 

def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    color = random_color()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.speed(0)

def left_mouse_click(x, y):
    draw_circle(x, y, 10)

turtle.hideturtle()

turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()