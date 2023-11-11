'''
Повторяющиеся буквы

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное 
выражение, которому соответствуют слова, содержащие повторяющиеся буквы.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/684549/tests_3182187.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.5/Module_11.5.15

regex = r''

Sample Input 1:
I have one apple, one banana and one strawberry
Sample Output 1:
apple banana strawberry

Sample Input 2:
Priveeeet my dear friend 
Sample Output 2:
Priveeeet

Sample Input 3:
fuisopf gheos, geisslp
Sample Output 3:
fuisopf geisslp
'''
regex = r'\b(\w)*(\w)(\w)*\2(\w)*\b'