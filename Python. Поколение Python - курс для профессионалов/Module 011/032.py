'''
Последовательности повторений

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное 
выражение, которому соответствуют строки, содержащие три или более последовательных 
повторений ok.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/684549/tests_3182178.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.5/Module_11.5.13

regex = r''

Sample Input 1:
Ok, Jim. I said okok! okokokok!
Sample Output 1:
okokokok

Sample Input 2:
OkoKokokOk OKOKOKOKK okokok
Sample Output 2:
okokok

Sample Input 3:
okokokoko okokokokkkkkk
Sample Output 3:
okokokok okokokok
'''
regex = r'(ok)\1{2,}'