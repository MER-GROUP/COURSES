Вложенные макеты
Любой макет можно вложить в другой макет. Давайте напишем небольшое приложение, где создадим три макета: Page Layout, Box Layout и Stack Layout. В Box Layout и Stack layout добавим по четыре кнопки. Далее добавим в Page Layout макеты Box Layout и Stack Layout:
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class NestedLayoutsApp( App ):
    def build(self):
        pl = PageLayout()

        bl = BoxLayout(orientation = 'vertical')
        btn = Button(text = 'Кнопка')
        btn2 = Button(text = 'Кнопка2')
        btn3 = Button(text = 'Кнопка3')
        btn4 = Button(text = 'Кнопка4')
        bl.add_widget(btn)
        bl.add_widget(btn2)
        bl.add_widget(btn3)
        bl.add_widget(btn4)

        sl = StackLayout(orientation = 'lr-bt' )
        btn5 = Button(text = 'Кнопка5',size_hint = ( 0.25 , 0.5 ))
        btn6 = Button(text = 'Кнопка6',size_hint = ( 0.25 , 0.5 ))
        btn7 = Button(text = 'Кнопка7',size_hint = ( 0.25 , 0.5 ))
        btn8 = Button(text = 'Кнопка8',size_hint = ( 0.25 , 0.5 ))
        sl.add_widget(btn5)
        sl.add_widget(btn6)
        sl.add_widget(btn7)
        sl.add_widget(btn8)

        pl.add_widget(bl)
        pl.add_widget(sl)
        return pl

if __name__ == '__main__':
    NestedLayoutsApp().run()
Результат:
