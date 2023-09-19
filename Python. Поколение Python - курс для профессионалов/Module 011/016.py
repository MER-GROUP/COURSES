'''
HTML-элементы

HTML-элементы — основа языка HTML. Каждый парный HTML-элемент обозначается 
начальным (открывающим) и конечным (закрывающим) тегами. Открывающий и закрывающий 
теги содержат имя элемента. Комментарии в страницах HTML помещаются между 
тегами <!-- и -->.

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют комментарии HTML.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680264/tests_3163820.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.3/Module_11.3.18

regex = r''

Sample Input 1:
Hi, your tags <!-bee-> and <--geek--> are incorrect. Correct tags look like <!--beegeek-->
Sample Output 1:
<!--beegeek-->

Sample Input 2:
<!-- header of page --> <-- incorrect header of page !-->
Sample Output 2:
<!-- header of page -->
'''
regex = r''