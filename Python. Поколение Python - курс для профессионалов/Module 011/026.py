'''
Строки 5

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют строки, удовлетворяющие следующим условиям:

строка начинается с Mr., Mrs., Ms., Dr. или Er.
оставшаяся часть строки состоит только из одной или более букв латинского алфавита 
в произвольном регистре
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/690796/tests_3166017.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.4/Module_11.4.17

regex = r''

Sample Input 1:
Mr.Guev
Sample Output 1:
Mr.Guev

Sample Input 2:
Ms.Jones
Sample Output 2:
Ms.Jones

Sample Input 3:
Dr. Guev
Sample Output 3:


Sample Input 4:
MRS.Traveler
Sample Output 4:
'''
regex = r'^(Mr|Mrs|Ms|Dr|Er)\.' + \
        r'[A-Za-z]+$'