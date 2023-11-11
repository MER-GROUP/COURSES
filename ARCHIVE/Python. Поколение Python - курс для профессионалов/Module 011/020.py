'''
Слова 2

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют слова, написанные строго заглавными латинскими буквами.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, 
окруженную символами, соответствующими \W

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/690796/tests_3166021.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.4/Module_11.4.11

regex = r''

Sample Input 1:
Why isn’t my progress in the APP synchrONized with my progress in the WEB version?
Sample Output 1:
APP WEB

Sample Input 2:
OOO 'BEEGEEK'
Sample Output 2:
OOO BEEGEEK

Sample Input 3:
I will go to the shop aNd you stay At home
Sample Output 3:
I
'''
regex = r'\b[A-Z]+\b'