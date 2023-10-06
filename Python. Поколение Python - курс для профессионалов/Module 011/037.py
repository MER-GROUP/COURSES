'''
Дважды подряд

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное 
выражение, которому соответствуют слова, записанные дважды подряд. 
Слова могут быть разделены одним или несколькими пробелами.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, 
окруженную символами, соответствующими \W

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/684549/tests_3182188.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.5/Module_11.5.18

regex = r''

Sample Input 1:
One can can become a writer only  only if he is   is talented
Sample Output 1:
can can only  only is   is

Sample Input 2:
f fa fa
Sample Output 2:
fa fa

Sample Input 3:
tuk tak
Sample Output 3:
'''
regex = r'\b(\w+)\b\s+\b\1\b'