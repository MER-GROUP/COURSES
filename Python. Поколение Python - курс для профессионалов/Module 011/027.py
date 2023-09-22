'''
Строки 6

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют строки, удовлетворяющие следующим условиям:

строка начинается с одной или двух цифр
после следуют три или более буквы латинского алфавита в произвольном регистре
оставшаяся часть строки содержит от 0 до 3 точек включительно

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/690796/tests_3166019.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.4/Module_11.4.18

regex = r''

Sample Input 1:
71mur...
Sample Output 1:
71mur...

Sample Input 2:
4rTur
Sample Output 2:
4rTur

Sample Input 3:
Python...
Sample Output 3:
'''
regex = r'^\d{1,2}' + \
        r'[A-Za-z]{3,}' + \
        r'\.{0,3}$'