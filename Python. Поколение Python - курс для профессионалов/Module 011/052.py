'''
HTML 🌶️🌶️

HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим) 
и конечным (закрывающим) тегами. Открывающий и закрывающий теги содержат имя элемента. 
Открывающий тег может содержать дополнительную информацию — атрибуты и значения атрибутов:

<b>BeeGeek</b>
<a href="https://stepik.org">Stepik</a>

В примере выше тег <b> не содержит никаких атрибутов, а тег <a> содержит 
атрибут href со значением https://stepik.org.

Напишите программу, которая находит во фрагменте HTML-страницы все атрибуты каждого тега.

Формат входных данных
На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.

Формат выходных данных
Программа должна найти в введенном фрагменте HTML-страницы все теги и вывести их, 
указав для каждого соответствующие атрибуты. Теги вместе со всеми атрибутами должны 
быть расположены каждый на отдельной строке, в следующем формате:

<тег>: <атрибут>, <атрибут>, ...

Теги, а также атрибуты тегов, должны быть расположены в лексикографическом порядке.

Примечание 1. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680265/tests_2898564.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.7/Module_11.7.17

Примечание 2. Некоторые теги не требуют закрытия. Об этом можно почитать здесь.
https://codebra.ru/ru/lessons-html/dating/2/1

Sample Input 1:
<p><a href="https://stepik.org">Stepik</a></p>
<div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>
Sample Output 1:
a: href
div: class
p:

Sample Input 2:
<div id="oldie-warning" class="do-not-print">
    <p>
        <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
        <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
    </p>
</div>
Sample Output 2:
a: href
div: class, id
em:
p:
strong:
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='052-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str.strip, stdin)
    sentense = stdin.read()
    print(sentense) # test
    pattern = rf''