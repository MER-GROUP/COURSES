Slider
Модуль: kivy.uix.slider

Slider - виджет у которого ползунок можно передвигать от минимального до максимального значения.
Атрибуты
orintation - принимает значение "horizontal"(горизонтальное положение) или "vertical"(вертикальное положение).
min - минимальное допустимое значение.
max - максимальное допустимое значение.
value - текущее используемое значения для слайдера. По умолчанию 0.
step - размер шага слайдера. По умолчанию 1.
События
on_touch_down - при нажатии на область слайдера
on_touch_up - при отпускании нажатии на область слайдера
on_touch_move - при перемещении ползунка слайдера
Пример
Создадим приложение где при перетаскивания ползунка на слайдере будет записываться его значение в Label:
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class SliderApp(App):
    def build(self):
        self.bl = BoxLayout(orientation = 'vertical' )
        self.s = Slider(min = 10, max = 80 ,value = 15 )
        self.label = Label(text = str(int(self.s.value)), font_size = '70sp' )
        self.s.bind(value = self.on_value)
        self.bl.add_widget(self.s)
        self.bl.add_widget(self.label)
        return self.bl
    def on_value(self,instance,value ):
        self.label.text = str(int(self.s.value))

if __name__ == '__main__':
    SliderApp().run()
Результат

