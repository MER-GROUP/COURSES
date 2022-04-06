Anchor Layout
Модуль: kivy.uix.anchorlayout

Anchor Layout - это макет, в котором виджеты могут быть привязаны к верху, низу, левому краю, правому краю или центру.
Атрибуты
anchor_x - привязывает виджет по горизонтали. Принимает значения "left", "center", "right".
anchor_y - привязывает виджет по вертикали. Принимает значения "top", "center", "bottom".
padding - внутренние отступы. Принимает список значений в пискелях "[padding_left, padding_top, padding_right, padding_bottom]".Так же можно назначить отступ по горизонтали и вертикали "[padding_horizontal, padding_vertical]" или одинаковое значение отступов со всех сторон "[padding]".
Методы
add_widget(widget) - добавляет виджет в макет.
remove_widget(widget) - удаляет виджет с макета.
Пример
Привяжем кнопку к верхнему левому углу:
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorLayoutApp( App ):
    def build( self ):
        al = AnchorLayout(anchor_x = 'left', anchor_y = 'top' )
        #Значения size_hint ставим в None чтобы кнопка не растягивалась на весь макет
        btn = Button(text = 'Кнопка', size_hint = (None,None))
        al.add_widget(btn)
        return al
if __name__ == '__main__':
    AnchorLayoutApp().run()
Результат:

