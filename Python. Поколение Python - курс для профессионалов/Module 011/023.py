'''
Строки 2

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют строки, удовлетворяющие следующим условиям:

строка начинается с двух или более цифр
после следуют ноль или более букв латинского алфавита в нижнем регистре
строка оканчивается нулем или более букв латинского алфавита в верхнем регистре
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/690796/tests_3166014.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.4/Module_11.4.14

regex = r''

Sample Input 1:
51tePIK
Sample Output 1:
51tePIK

Sample Input 2:
79
Sample Output 2:
79

Sample Input 3:
stePIK
Sample Output 3:
'''
regex = r'^\d{2,}' + \
        r'[a-z]*' + \
        r'[A-Z]*$'