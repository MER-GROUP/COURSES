Первое приложение
Напишем первое приложения, где по нажатию кнопки будем записывать текст из виджета text input в виджет label:
#Импортируем класс App из модуля kivy.app
from kivy.app import App
#Импортируем класс BoxLayout из модуля kivy.uix.boxlayout
#Все layouts(макеты) находятся в пакете kivy.uix
from kivy.uix.boxlayout import BoxLayout
#Импортируем класс TextInput из модуля kivy.uix.textinput для ввода текста
from kivy.uix.textinput import TextInput
#Импортируем класс Label из модуля kivy.uix.label для отображения текста
from kivy.uix.label import Label
#Импортируем класс Button из модуля kivy.uix.button.Обычная кнопка
fromkivy.uix.button import Button
#Все виджеты также находятся в пакете kivy.uix

#Создаем класс.Обязательно что бы названия класса заканчивалось на App
#В нашем случае приложение называется First и если вы запустите приложение то в левом верхнем углу увидите название приложения
class FirstApp(App):
    def build(self):
        #Создаем макет BoxLayout и в качестве атрибута orientation установим vertical
        #Все виджеты будут распологаться по порядку по вертикали
        bl = BoxLayout(orientation = 'vertical')
        #Создаем виджеты
        self.text_input = TextInput()
        self.label = Label()
        #Для кнопки зададим текст 'Ok' и атрибуту on_press наш созданный далее метод
        self.button = Button(text = 'Ok', on_press = self.click)
        #Добавляем в наш созданный макет c помощью метода add_widget сначало текст ввода,потом лейбл и кнопку
        bl.add_widget(self.text_input)
        bl.add_widget(self.label)
        bl.add_widget(self.button)
        #Отображаем наш макет с виджетами
        return bl
    #В данном методе присваеваем текст из виджета ввода текста в виджет лейбл
    def click(self, event ):
        self.label.text = self.text_input.text

#Создаем экземляр класса FirstApp и запускаем метод run.
if __name__ == "__main__":
    FirstApp().run()
Сначало импортируем класс App из модуля kivy.app. Далее виджеты и макет Box Layout из пакета kivy.uix и соответствущих модулей. Создаем класс FirstApp (обязательно название с класса должно заканчиваться на App) и наследуемся от класса App. Cоздаем метод build который должен возвращать виджет или макет для отображения. Без этого метода мы не сможем запустить наше приложения. В этом методе так же создаем наш Box Layout, Text Input, Label,Button. Добавляем в макет Box Layout все созданные виджеты и с помощью ключевого слова return возвращаем Box Layout
Так же создаем метод click в котором при нажатии на кнопку, текст введенный в Text Input, будет отображаться в Label. И кнопке атрибуту on_press присваиваем название нашего метода click. Далее создаем экземпляр класса и вызываем метод run (FirstApp().run())
Результат:
