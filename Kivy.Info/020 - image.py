Image
Модуль: kivy.uix.image

Image - используется для отображения изображения.
Атрибуты
source - принимает в качестве значения путь к изображению в виде строки.
allow_stretch - если значения "True", нормализованный размер изображения будет максимально увеличен, чтобы поместиться в поле изображения. Если "False" то изображение не будет растягиваться более чем на 1:1 пиксель.
Методы
reload() - перезагружает изображение с диска. Это облегчает повторную загрузку изображений с диска в случае изменения содержимого изображения.
Пример
Создадим приложения где загрузим изображения с диска и растяним его:
from kivy.app import App
from kivy.uix.image import Image

class ImageApp(App):
    def build(self):
        img = Image(source = 'imageexample.png', allow_stretch = True )
        return img
if __name__ == '__main__':
    ImageApp().run()
Результат

Async Image
Модуль: kivy.uix.image
Async Image - используется для загрузки изображения с интернета в фоновом потоке.
async_image = AsyncImage(source = 'URL изображения' )
