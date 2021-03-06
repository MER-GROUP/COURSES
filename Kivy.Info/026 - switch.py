Switch
Модуль: kivy.uix.switch

Switch - виджет который представляет собой переключатель, где "on"(включен) и "off"(выключен)
Атрибуты
active - принимает значение "True" или "False". Если значение "True", то switch переключаеться на "on". Если "False", то на "off". По умолчанию "False".
Методы
bind(событие = название метода) - с помощью метода bind можно привязать к событию метод.
Пример
Напишем приложение, где при переключении switch будет меняться цвет фона. Если переключатель будет в позиции "on" то цвет фона будет белый, а если "off" черный. Для того чтобы менять цвет фона импортируем класс Window из модуля kivy.core.window. У класса Window есть атрибут clearcolor который принимает в качестве значения list(цвет в формате RGBA):
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.switch import Switch

class SwitchApp(App):
    def build(self):
        switch = Switch(active = False )
        switch.bind(active = self.on_active)
        return switch

    #Создадим метод, где если атрибут active будет в позиции "on" фон станет белым цветом иначе если "off" черным
    def on_active(self,instance, value):
        if value:
            #Метод clearcolor принимает в качестве значения list(цвет в формате RGBA).Значение от 0 до 1, где один равен значение 255.
            #Получается если нам нужен белый цвет(255,255,255) то значение будет (1,1,1,1),если черный то (0,0,0,1)
            Window.clearcolor = (1,1,1,1)
        else:
            Window.clearcolor = (0,0,0,1)

if __name__ == '__main__':
    SwitchApp().run()
Результат:

