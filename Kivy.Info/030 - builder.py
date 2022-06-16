Класс Builder
Модуль: kivy.lang.builder
Класс Builder позволяет загружать файл Kv Design Language,а так же с помощью метода load_string напрямую писать разметку.
Методы
load_file('путь к файлу') - позволяет загружать файл с расширением ".kv".
load_string("""разметка""") - в качестве параметра пишем разметку Kv Design Language.
Пример
Создадим файл с разметкой example.kv:
#:kivy 1.10.0
BoxLayout:
    orientation:'horizontal'
    Button:
        text:"Click"
Создадим файл builder_app.py и загрузим нашу разметку example.kv с помощью метода load_file и присвоем переменной example_kv:
from kivy.app import App
from kivy.lang.builder import Builder

example_kv = Builder.load_file('example.kv')

class BuilderApp(App):
    def build(self):
        return example_kv

if __name__ == '__main__':
    BuilderApp().run()
Так же с помощью метода load_string попробуем написать разметку напрямую:
from kivy.app import App
from kivy.lang.builder import Builder

example_kv = Builder.load_string("""
#:kivy 1.10.0
BoxLayout:
    orientation:'horizontal'
    Button:
        text:"Click"
""")

class BuilderApp(App):
    def build(self):
        return example_kv

if __name__ == '__main__':
    BuilderApp().run()
Результат:

