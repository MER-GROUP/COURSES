'''
Строки 3

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют строки, удовлетворяющие следующим условиям:

строка содержит исключительно буквы латинского алфавита в произвольном регистре
строка оканчивается латинской буквой s в нижнем регистре
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/690796/tests_3166015.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.4/Module_11.4.15

regex = r''

Sample Input 1:
Chess
Sample Output 1:
Chess

Sample Input 2:
exodus
Sample Output 2:
exodus

Sample Input 3:
Diablo
Sample Output 3:
'''
regex = r'^[A-Za-z]*' +\
        r's$'