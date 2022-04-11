Relative Layout
Модуль: kivy.uix.relativelayout

Relative Layout - это макет, в котором виджеты располагаются относительно начальной позиции макета. По умолчанию начальная позиция с координатами (0,0) левый нижний угол и все виджеты изначально будут расположены в этих координатах. Но если мы зададим для кнопки свою позицию, то кнопка сдвинеться относительно начальной координаты на столько пикселей, сколько задали в атрибуте pos.
Атрибуты
size - принимает значение ширины и высоты макета в виде кортежа.
pos - принимает значение координат по х и y в виде кортежа.
Методы
add_widget(widget) - добавляет виджет в макет.
remove_widget(widget) - удаляет виджет с макета.
to_local( x , y , ** k ) - преобразует родительские координаты в локальные.
to_parent( x , y , ** k ) - преобразует локальные координаты в родительские.
Пример
Чтобы разобраться в Relative Layout напишем пример, где зададим начальную позицию макета по х и y в 200 пикселей. Так же создадим три кнопки. Первая кнопка будет на начальной позиции, вторую сдвинем на 100 пиксей, а третью на 200:
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class RelativeLayoutApp( App ):
    def build( self ):
        rl = RelativeLayout(pos = (200 ,200))
        btn = Button (text = 'Кнопка',size_hint = (None ,None))
        btn2 = Button (text = 'Кнопка2',size_hint = (None ,None), pos = (100, 100 ))
        btn3 = Button (text = 'Кнопка3',size_hint = (None ,None), pos = (200, 200))
        rl.add_widget(btn)
        rl.add_widget(btn2)
        rl.add_widget(btn3)
        return rl

if __name__ == '__main__':
    RelativeLayoutApp().run()
Результат:

