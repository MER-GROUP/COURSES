'''
Последовательность цифр

Дополните приведенный ниже код, чтобы переменная regex содержала 
регулярное выражение, которому соответствуют последовательности цифр, 
представляющие целые числа от 100 до 199 включительно.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640164/tests_2829463.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.1/Module_11.1.23

regex = r''

Sample Input 1:
150 + 1000 = 1150
Sample Output 1:
150 100 115

Sample Input 2:
100 - 199
Sample Output 2:
100 199
'''
regex = r'1\d\d'