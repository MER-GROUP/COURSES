Accordion
Модуль: kivy.uix.accordion

Accordion - представляет собой форму меню, в котором параметры располагаются вертикально или горизонтально, а при нажатии на элемент открывается для отображения его содержимое.Accordion состоит из элементов AccordionItem. В AccordionItem можно помещать, как виджеты, так и макеты.
Структура
Accordion:
    AccordionItem:
        Контент(виджеты или макеты)
    AccordionItem:
        BoxLayout(макет):
                Контент(виджеты или макеты)
Атрибуты
orientation - принимает значение "horizontal"(горизонтальное расположение элементов) или "vertical"(вертикальное расположение элементов).
anim_duration - продолжительность анимации в секундах при выборе нового элемента аккордеона. По умолчанию 0.25 (250мс).
min_space - минимальное пространство для заголовка каждого элемента. Это значение автоматически устанавливается для каждого дочернего элемента каждый раз, когда происходит событие макета. По умолчанию 44 px.
Методы
add_widget(AccordionItem) - добавляет элемент Accordion Item.
remove_widget(AccordionItem) - удаляет элемент Accordion Item.
AccordionItem
Атрибуты
title - заголовок элемента меню.
Методы
add_widget(Widget) - добавляет виджет или макет.
remove_widget(Widget) - удаляет виджет или макет.
Пример
Создадим Accordion и добавим в него два AccordionItem. Добавим в каждый AccrodionItem макет Box Layout. В один Box Layout поместим три кнопки, а в другой три лейбла:
from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class AccordionApp(App):
    def build(self):
        accordion = Accordion(orientation = 'vertical')
        bl = BoxLayout(orientation = 'vertical')
        btn = Button(text = 'Кнопка' )
        btn2 = Button(text = 'Кнопка2')
        btn3 = Button(text = 'Кнопка3')
        bl.add_widget(btn)
        bl.add_widget(btn2)
        bl.add_widget(btn3)
        accordion_item = AccordionItem(title = "Кнопки" )
        accordion_item.add_widget(bl)

        bl2 = BoxLayout(orientation = 'vertical')
        label = Label(text = 'Строка' )
        label2 = Label(text = 'Строка2')
        label3 = Label(text = 'Строка3')
        bl2.add_widget(label)
        bl2.add_widget(label2)
        bl2.add_widget(label3)
        accordion_item2 = AccordionItem(title = "Строки" )
        accordion_item2.add_widget(bl2)

        accordion.add_widget(accordion_item)
        accordion.add_widget(accordion_item2)
        return accordion

if __name__ == '__main__':
    AccordionApp().run()
Результат:

