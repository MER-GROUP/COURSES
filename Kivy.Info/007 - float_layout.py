Float Layout
Модуль: kivy.uix.floatlayout

Float Layout - это макет в котором вы сами задаете позицию виджета. Вы также можете расположить виджеты поверх других виджетов.
Атрибуты
size - принимает значение ширины и длины макета в виде кортежа.
Методы
add_widget(widget) - добавляет виджет в макет.
remove_widget(widget) - удаляет виджет с макета.
Пример
Создадим макет Float Layout и зададим размер по ширине и высоте в 300 пикселей ,в котором расположим две кнопки. Одной кнопке установим фиксированую позицию pos по x и по y значение 50 , а другую кнопку установим по центру с помощью pos_hint:
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
class FloatLayoutApp(App ):
    def build(self):
        fl = FloatLayout(size = (300 , 300 ))
        #Установим первой и второй кнопке размер size_hint в 20%(0.2) от размера макета по ширине и высоте
        btn = Button(text = 'Кнопка' ,size_hint = (0.2 ,0.2), pos = ( 50 ,50))
        btn2 = Button(text = 'Кнопка2' ,size_hint = (0.2 ,0.2), pos_hint = { 'center_x': 0.5 , 'center_y' :0.5})
        fl.add_widget(btn)
        fl.add_widget(btn2)
        return fl
if __name__ == '__main__':
    FloatLayoutApp().run()
Результат:

