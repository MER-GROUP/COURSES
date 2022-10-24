import random as r
import turtle as t

def go(x0, y0):
    # Идти на координаты
    t.up()
    t.goto(x0, y0)
    t.down()

def move(x0, y0):
    # Пододвинуться
    x, y = t.pos()
    go(x + x0, y + y0)

def simple_starry_sky(count, color='White'):
    # Рассыпать точки по небу
    for _ in range(count):
        size = r.randrange(1, 5)
        # color = (r.randrange(200, 256), r.randrange(200, 256), r.randrange(200, 256))
        go(r.randrange(-1280 / 2, 1280 / 2), r.randrange(-720 / 2, 720 / 2))
        t.dot(size, color)

def rectangle(width, height, pen='Black', fill='White'):
    # Построить прямоугольник
    t.color(pen, fill)
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def home_alone_background(size):
    # Параметры окна - - - - - - - - - - - -
    t.Screen().title('Задник, как в «Одном дома»')  # Склонения - наше всё
    Screen_x = 1280
    Screen_y = 720
    t.Screen().setup(Screen_x, Screen_y)
    t.Screen().colormode(255)
    t.tracer(0)
    t.ht()
    # Мясо функции - - - - - - - - - - - - -

    'Россыпь звёзд чисто по границе выводимого окна (вроде)'
    simple_starry_sky(1000, color='yellow')

    'Настройка цветовой палитры'
    house_color = (20, 20, 160)
    window_color = (255, 255, 150)
    background_color = (5, 5, 70)
    t.pencolor(background_color)
    t.bgcolor(background_color)

    go(-Screen_x / 2, -Screen_y / 2)
    width = size / 1.884  # Миллиметры ¯\_(ツ)_/¯
    while t.xcor() < Screen_x / 2 - width:

        'Постановка блоков панельных квартир'
        height = size * r.randrange(2, 7)
        rectangle(width, height, pen=house_color, fill=house_color)

        'Открытие окон'
        x, y = t.pos()
        while t.ycor() < height - Screen_y // 2 - size / 5:  # Криво, но так окна хотя бы выше крыши не открываются
            move(0, size / 5)
            if r.choice([True, False, False]):  # Наглядный шанс открыть окно в принципе
                for _ in '50':  # 50/50 шанс открыть окно ещё и на соседней позиции
                    go(r.choice([x + width / 6, x + width / 1.5]), t.ycor())
                    rectangle(size / 10, size / 10, pen=window_color, fill=window_color)

        'Спасибо этому дому, пойдём к другому'
        go(x, y)
        move(width, 0)

    'Дополнение картины'
    text_size = 5000 // size  # Соразмерность домов и текста
    go(0, Screen_y / 2 - text_size * 2)
    t.pencolor('Yellow')
    t.write('HOME🏠ALONe', align='center', font=('Times New Roman', text_size, 'underline', 'bold'))

crop = int(input('''\n\033[1;30;42mМасштаб панелек относительно окна.\033[0;0m
\033[3;37m Оптимально при crop ∈ [50, 100] \033[0;0m \n  > '''))  # t.numinput() не будет
home_alone_background(crop)
t.done()