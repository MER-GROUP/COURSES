Modal View
Модуль: kivy.uix.modalview

Modal View - виджет который из себя представляет модальное окно.
Атрибуты
auto_dismiss - принимает значение "True" или "False". Если значение "True", то кликнув на любой области в окне приложения модальное окно закроется. Если "False", то модальное окно не будет закрываться пока не будет вызван метод dismiss.
Методы
open() - открывает модальное окно.
dismiss() - закрывает модальное окно.
add_widget() - добавляет в модальное окно виджет(макет).
События
on_touch_down - при нажатии на Modal View
on_touch_up - при отпускании нажатии на Modal View
on_touch_move - при перемещении Modal View
Пример
Создадим приложение, где добавим кнопку для открытия модального окна. В модальное окно добавим макет Box Layout, а в него label и кнопку для закрытия модального окна:
from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ModalViewApp( App):
    def build(self):
        #Cоздаем модальное окно и атрибуту auto_dismiss присваиваем значение False для того чтобы окно закрывалось только по нажатию кнопки
        modal = ModalView(size_hint=(None ,None), size =(400 ,400), auto_dismiss=False)
        bl = BoxLayout(orientation ='vertical', size_hint=(None ,None))
        label = Label(text='Модальное окно', size_hint=(None ,None))
        btn_close = Button(text='Закрыть', size_hint=(None ,None))
        #Привязываем событию по нажатию на кнопку метод закрытия модального окна
        btn_close.bind(on_press=modal.dismiss)
        #Добавляем label и кнопку закрытия модального окна в Box Layout
        bl.add_widget(label)
        bl.add_widget(btn_close)
        #Добавляем в модальное окно макет Box Layout
        modal.add_widget(bl)
        #Создаем кнопку открытия модального окна и привязываем событию по нажатию на копку метод открытия модального окна
        btn_open = Button(text = 'Открыть модальное окно', size_hint=(None , None), size=( 200 , 100 ), pos_hint = {'x' : 0.37 , 'y' : 0 })
        btn_open.bind(on_press = modal.open)
        return btn_open

if __name__ == '__main__':
    ModalViewApp().run()
Результат:

