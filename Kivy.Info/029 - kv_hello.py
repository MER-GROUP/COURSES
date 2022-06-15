Первое приложение c Kv Design Language
Напишем первой приложение с Kv Design Language. Для начала создадим файл myapp.py, где напишем такой код:
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#Пустой класс для которого будем создавать разметку с помощью Kivy Design Language.
#Данный класс наследуется от макета Box Layout
class Example(BoxLayout):
    pass

#Основной класс с методом build который возвращает экземляр класса Example
class MyApp( App ):
    def build( self ):
        example = Example()
        return example

if __name__ == '__main__':
    MyApp().run()
Далее в той же папке где лежит файл myapp.py создадим файл my.kv. Название файла Kv Deisgn Language должен быть в нижнем регистре и должен совпадать с названием класса в нашем случае MyApp (например есть класс будет называться ExampleApp тогда файл Kv Design Language будет называться example.kv). Причем окончание App писать ненужно. Далее напишем разметку:
#:kivy 1.10.0
<Example>:
    orientation:'vertical'
    pos_hint: { 'center_x' : 1 ,'center_y':1 }
    Button:
        text: 'hello'
        size_hint:(None,None)
    Button:
        text:'kivy'
        size_hint:(None,None)
Сначало пишем наш пустой класс созданный в myapp.py в угловых скобках. Далее прописываем атрибуты ориентации и позицию по центру.Внутри класса создаем две кнопки и у них так же прописываем атрибуты. Запускаем myapp.py и вот что в итоге должно получиться:

