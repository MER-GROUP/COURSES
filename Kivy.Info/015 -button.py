Button
Модуль: kivy.uix.button

Button - кнопка при нажатия которой, происходит назначенное на эту кнопку событие.
Атрибуты
text - текст который отображается на кнопке.
font_size - размер шрифта текста на кнопке.
on_press - событие при нажатие на кнопку. Принимает в качестве значения названия метода.
on_release - событие при отпускания нажатия на кнопку. Принимает в качестве значения названия метода.
Методы
bind(событие = название метода) - с помощью метода bind можно привязать к событию метод.
Cобытия
on_press - событие происходит при нажатии на кнопку
Пример
Создадим кнопку при нажатие на которую текст кнопки будет меняться на "Ок":
from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build( self ):
        self.btn = Button(text ='Кнопка')
        self.btn.bind(on_press = self.click)
        return self.btn
    def click (self, instance ):
        self.btn.text = "Ok"

if __name__ == '__main__':
    ButtonApp().run()
Результат:

