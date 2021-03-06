Spinner
Модуль: kivy.uix.spinner

Spinner - это виджет, который обеспечивает быстрый способ выбора одного значения и списка.
Атрибуты
is_open - если "True", то спиcок spinner изначально будет открыт. Если "False",то закрыт. По умолчанию "False".
values - принимает в качестве значаения список , который будет отображаться для выбора элемента из списка.
Методы
bind(событие = название метода) - с помощью метода bind можно привязать к событию метод.
Пример
Напишем приложение, где при выборе элемента из списка spinner текст будет выводиться в label:
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label

class SpinnerApp(App):
    def build(self):
        fl = FloatLayout()
        self.spinner = Spinner(text = "First", values =("First","Second", "Third"),size_hint = (0.3,0.2), pos_hint ={'center_x': 0.5 ,'center_y':0.5})
        self.label = Label(text = self.spinner.text,size_hint = (0.3, 0.2 ), pos_hint = {'center_x': 0.5 , 'center_y': 0.8 })
        self.spinner.bind(text = self.on_selected_spinner)
        fl.add_widget(self.spinner)
        fl.add_widget(self.label)
        return fl

    def on_selected_spinner(self, spinner, text):
        self.label.text = text

if __name__ == '__main__':
    SpinnerApp().run()
Результат:

