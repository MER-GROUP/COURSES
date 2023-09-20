'''
Время

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют времена формата HH:MM.

Примечание 1. Требуется дополнительная проверка на корректность, то есть 
время 54:96 не должно соответствовать регулярному выражению regex.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/683127/tests_2833102.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.2/Module_11.2.22

regex = r''

Sample Input 1:
So why does my watch say 91:44? It doesn't matter, I'll be there at 17:30
Sample Output 1:
17:30

Sample Input 2:
00:00, 00:60, 24:00, 50:39, 17/30
Sample Output 2:
00:00
'''
# 00:00
# 09:59

# 10:00
# 19:59

# 20:00
# 23:59
regex = r'[01]\d:[0-5]\d|' \
        r'2[0-3]:[0-5]\d'