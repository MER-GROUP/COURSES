Code Input
Модуль kivy.uix.codeinput

Code Input - виджет в котором можно писать код с подсветкой для определенного языка программирования. Для того что бы менять подсветку языка нужно так же установить модуль Pygments. Для этого вводим в консоли pip install pygments
Атрибуты
lexer - содержит выбранный лексер(подсветку для определенного языка программирования. Например если нам нужна подсветка для языка Java, то присваеваем "JavaLexer()"). По умолчанию в качестве значения принимает "PythonLexer()".
Пример
Создадим Code Input с подсветкой языка программирования Python:
from kivy.app import App
from kivy.uix.codeinput import CodeInput
from pygments.lexers import PythonLexer

class CodeInputApp(App):
    def build(self):
        code_input = CodeInput(lexer = PythonLexer())
        return code_input

if __name__ == '__main__':
    CodeInputApp().run()
Результат

