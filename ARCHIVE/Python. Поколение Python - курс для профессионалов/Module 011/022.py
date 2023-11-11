'''
Строки

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют строки, содержащие открывающую круглую скобку, 
а за ней когда-нибудь закрывающую круглую скобку.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/690796/tests_2883600.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.4/Module_11.4.13

regex = r''

Sample Input 1:
(41 + 9) * 2 = ?
Sample Output 1:
(41 + 9) * 2 = ?

Sample Input 2:
A synthesizer (also spelled synthesiser) is an electronic musical instrument that generates audio signals.
Sample Output 2:
A synthesizer (also spelled synthesiser) is an electronic musical instrument that generates audio signals.

Sample Input 3:
It was to be both a technical and surprisingly emotional challenge!))
Sample Output 3:
'''
regex = r'.*\(.*\).*'