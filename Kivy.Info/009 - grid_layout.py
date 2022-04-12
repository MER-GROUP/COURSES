Grid Layout
Модуль: kivy.uix.gridlayout

Grid Layout - это макет, который располагает виджеты в виде ячеек в таблице. Можно задать количество строк(rows) и количество столбцов(cols)
Атрибуты
cols - задает количество столбцов.
rows - задает количество строк.
col_default_width - задает минимальну ширину в столбце по умолчанию.
col_force_default - принимает значение "True" или "False". Если значение "True", то столбец игнорирует ширину и атрибут size_hint_x виджета и использует по умолчанию ширину столбца.
cols_minimum - принимает в качестве значения словарь, где каждому столбцу можно присвоить минимальную ширину. Ключом будет номер столбца.
row_default_height - задает минимальныу высоту строки по умолчанию.
row_force_default - принимает значение "True" или "False". Если значение "True", то строка игнорирует высоту и атрибут size_hint_y у виджета и использует по умолчанию высоту строки.
rows_minimum - принимает в качестве значения словарь, где каждой строке можно присвоить минимальную высоту. Ключом будет номер строки.
padding - внутренние отступы. Принимает список значений в пискелях "[padding_left, padding_top, padding_right, padding_bottom]".Так же можно назначить отступ по горизонтали и вертикали "[padding_horizontal, padding_vertical]" или одинаковое значение отступов со всех сторон "[padding]".
spacing - расстояние между виджетами. Принимает список значений в пискелях по горизонтали и вертикали "[spacing_horizontal, spacing_vertical]". Так же можно задачть только одно значение "[spacing]", которое будет применяться по горизонтали и вертикали.
Методы
add_widget(widget) - добавляет виджет в макет.
remove_widget(widget) - удаляет виджет с макета.
Пример
Создадим макет Grid Layout и установим размер столбцов (cols) в значение 2. Добавим в макет четыре кнопки:
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayoutApp(App):
    def build(self ):
        gl = GridLayout(cols= 2 )
        btn = Button(text = 'Кнопка' )
        btn2 = Button(text = 'Кнопка2' )
        btn3 = Button(text = 'Кнопка3' )
        btn4 = Button(text = 'Кнопка4' )
        gl.add_widget(btn)
        gl.add_widget(btn2)
        gl.add_widget(btn3)
        gl.add_widget(btn4)
        return gl

if __name__ == '__main__':
    GridLayoutApp().run()
Результат:

Как вы заметили мы здесь не меняли у кнопок атрибут size_hint .По умолчание size_hint = "(1,1)", что означает по ширине и высоте 100%. При таком значении в данном макете кнопка будет растягиваться на всю ячеейку.
