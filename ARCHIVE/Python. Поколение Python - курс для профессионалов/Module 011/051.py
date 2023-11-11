'''
HTML 🌶️

HTML-элементы — основа языка HTML. Каждый HTML-элемент обозначается начальным (открывающим) 
и конечным (закрывающим) тегами. Открывающий и закрывающий теги содержат имя элемента. 
Открывающий тег может содержать дополнительную информацию — атрибуты и значения атрибутов. 
Гиперссылки в языке HTML создаются с помощью тега <a></a>. Внутрь помещается текст, 
который будет отображаться на веб-странице. Обязательной составляющей 
тега <a></a> является атрибут href, который задает URL-адрес веб-страницы:

<a href="https://stepik.org">Stepik</a>  

Гиперссылка состоит из двух частей — указателя (Stepik) и адресной части (https://stepik.org). 
Указатель ссылки представляет собой фрагмент текста или изображение, видимые для пользователя. 
Адресная часть ссылки пользователю не видна, она представляет собой адрес ресурса, к которому 
необходимо перейти. Иногда указатель может быть окружен различными тегами (<b></b>, <h1></h1>):

<a href="https://stepik.org"><b><h1>Stepik</h1></b></a>

Напишите программу, которая находит во фрагменте HTML-страницы все гиперссылки и выводит 
их составляющие — адресные части и указатели.

Формат входных данных
На вход программе подается произвольное количество строк, которые образуют фрагмент HTML-страницы.

Формат выходных данных
Программа должна найти во введенном фрагменте HTML-страницы все гиперссылки и вывести 
их составляющие — адресные части и указатели, в следующем формате:

<адресная часть>, <указатель>
<адресная часть>, <указатель>
...

Примечание 1. Порядок следования данных об очередной гиперссылке должен совпадать 
с порядком их следования в введенном фрагменте HTML-страницы.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680265/tests_2898556.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.7/Module_11.7.16

Sample Input 1:
<p><a href="https://stepik.org">Stepik</a></p>
<p><a href="https://beegeek.ru"><b>BEEGEEK</b></a></p>
Sample Output 1:
https://stepik.org, Stepik
https://beegeek.ru, <b>BEEGEEK</b>

Sample Input 2:
<div id="oldie-warning" class="do-not-print">
    <p>
        <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
        <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
    </p>
</div>
Sample Output 2:
http://browsehappy.com/, upgrade to a different browser
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='051-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str.strip, stdin)
    sentense = stdin.read()
    # print(*sentense) # test
    # pattern = rf'<a href=\"([\w.:/]+)\">(.*(\w).*)?</a>'
    # pattern = rf'<a href=\"([\w.:/]+)\">(((\w+))|(.*>(\w+)<.*))?</a>'
    # pattern = rf'<a href=\"([\w.:/]+)\">((\w+)|(.*>(\w+)<.*))?</a>'
    # pattern = rf'<a href=\"([\w.:/]+)\">((\w+)|(.+>(\w+)<.+))?</a>'
    # pattern = rf'<a href=\"([\w.:/]+)\">(([\w\s]+)|(.+>([\w\s]+)<.+))?</a>'
    # pattern = rf'<a href=\"([\w.:/]+)\">(([\w\s]+)|(.+?>+?([\w\s]+)<+?.+?))?</a>'
    # pattern = rf'<a href=\"([\w.:/]+)\">(([\w\s]+)|(.+?>+?([\w\s]+)<+?.+?))?</a>'

    # pattern = rf'<a href=\"([\w.:/]+)\">(.*?)</a>'
    pattern = rf'<a href=\"(.*)\">(.*?)</a>'

    match = re.finditer(pattern, sentense, re.MULTILINE)
    # print(*match)
    for it in match:
        # print(it.groups())
        print(", ".join(it.group(1, 2)))
        # if it.group(3):
        #     print(", ".join(it.group(1, 3)))
        # else:
        #     print(", ".join(it.group(1, 5)))