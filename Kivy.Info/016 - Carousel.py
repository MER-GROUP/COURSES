Carousel
Модуль: kivy.uix.carousel

Carousel - виджет, в котором можно пролистывать вложенные в него элементы.
Атрибуты
direction - определяет направление, переключения слайдов.Принимает одно из значений "right","left","top","bottom".
ignore_perpendicular_swipes - игнорирует движение перпендикулярно по оси.
index - позволяет получить или установить текущий основной слайд. По умолчанию 0.
loop - повзоляет прокручивать карусель бесконечно.Если значение "True", когда пользователь попытаеться пролистать за последнюю страницу, он вернется к первой. Если "False", он останется на последней странице.
slides - список слайдов внутри карусели. Слайды - это виджеты, добавленные в карусели с использованием "add_widget" метода.
Методы
add_widget(widget) - добавляет виджет в макет.
remove_widget(widget) - удаляет виджет с макета.
load_next(mode = "next") - анимировать до следующего слайда.
load_previous - анимировать к предыдущему слайду.
load_slide(слайд) - анимировать слайд, который передается в качстве значения.
События
on_touch_down - при нажатии на carousel
on_touch_up - при отпускании нажатии на carousel
on_touch_move - при переключение слайдов carousel
Пример
Создадим Carousel и добавим в него три кнопка. Направления перелистывание установим в "top" и атрибут loop устрановим в "True", чтобы можно было перелистывать слайды бесконечно:
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button

class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction = 'top',loop = True )
        btn = Button(text ='Кнопка')
        btn2 = Button(text ='Кнопка2')
        btn3 = Button(text ='Кнопка3')
        carousel.add_widget(btn)
        carousel.add_widget(btn2)
        carousel.add_widget(btn3)
        return carousel

if __name__ == '__main__':
    CarouselApp().run()
Результат

