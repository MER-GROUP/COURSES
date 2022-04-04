Настройка размера экрана
Есть два способа задать размер окна. Первый способ это перед созданием приложения. Импортируем класс Config из модуля kivy.config:
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

#У класса Config вызываем метод set и первым параметром пишем к чему обращаемся в данном случае к graphics
#Устанавливаем width(ширину) и height(длину) в 100 пикселей
Config.set('graphics','width','100')
Config.set('graphics','height','100')

class TestApp(App):
    def build(self ):
        bl = BoxLayout()
        return bl
if __name__ == '__main__':
    TestApp().run()
Так же можно запретить или разрешить растягивания экрана для этого также обращаемся к "graphics" и к параметру "resizable". И третим параметром пишем "True" (разрешить растягивание) или "False" чтобы запретить растягивание.
Config.set('graphics','resizable',False)
Второй способ это динамически изменить размер после создания окна. Для этого импортируем класс Window из модуля kivy.core.window:
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class TestApp( App ):
    def build( self ):
        bl = BoxLayout()
        return bl

Window.size = ( 200 , 100)

if __name__ == '__main__':
    TestApp().run()
