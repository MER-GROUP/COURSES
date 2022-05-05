Color Picker
Модуль: kivy.uix.colorpicker

Color Picker - позволяет пользователю выбирать цвет из хроматического колеса, где пинч и масштаб могут использоваться для изменения насыщенности колеса. Ползунки и поля ввода также предусмотрены для непросредственного ввода значений в форматах RGBA/HSV/HEX.
Атрибуты
color - устанавливает изначальный свет при запуске приложения в формате RGBA (от 0 до 1). Принимает числовой картеж в виде (красный, зеленый, синий, прозрачность). По умолчанию установлено (1,1,1,1).
font_name - указывает шрифт, используемый в Color Picker. По умолчанию путь к шрифту "data/fonts/RobotMono-Regular.ttf".
hex_color - устанавливает цвет в шестнадцатеричном формате. По умолчанию "#ffffff".
hsv - устанавливает цвет в hsv(hue(оттенок),saturation(насыщенность), value(значение)) формате (от 0 до 1). По умолчанию (1,1,1).
Пример
Создадим Color Picker, где по умолчанию поставим красный цвет в шестнадцатеричном формате и будем менять цвет:
from kivy.app import App
from kivy.uix.colorpicker import ColorPicker

class ColorPickerApp(App):
    def build(self):
        color_picker = ColorPicker(hex_color = '#ff0000' )
        return color_picker

if __name__ == '__main__':
    ColorPickerApp().run()
Результат

