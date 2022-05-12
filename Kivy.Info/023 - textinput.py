Text Input
Модуль: kivy.uix.textinput

Text Input - виджет для ввода текста
Атрибуты
multiline - если значение "True", то разрешаеться многострочный ввод. Если "False", то однострочный.
allow_copy - если значение "True", то разрешаеться копирование текста.Если "False", то нет. По умолчанию "True".
auto_indent - если значение "True", то включаеться автоматический отступ многострочного текста. Если "False", то нет. По умолчанию "True".
cursor - кортеж из "(строка,столбец)" указывающих текущую позицию курсора.
cursor_blink - если значение "True", то курсор будет моргать. Если "False", то нет.
События
on_text_validate - срабатывает когда пользователь нажал на клавишу Enter.При этом значение атрибута multiline должно быть равно False
on_touch_down - срабатывает при нажатии на Text Input
on_touch_up - срабатывает при отпускании нажатии на Text Input
on_double_tap - срабатывает при двойном нажатии на Text Input
on_triple_tap - срабатывает при тройном нажатии на Text Input
on_quad_touch - срабатывает когда четыре пальца касаются Text Input
Пример
Создадим приложение с Text Input. Установим многострочный ввод текста и размер шрифта "50sp":
from kivy.app import App
from kivy.uix.textinput import TextInput

class TextInputApp( App ):
    def build(self):
        text_input = TextInput(multiline = True, font_size = "50sp")
        return text_input

if __name__ == '__main__':
    TextInputApp().run()
Результат

