'''
Последовательность символов 2

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности символов длины 5, удовлетворяющие 
следующим условиям:

первый символ — строчная латинская буква
второй символ — произвольная цифра
третий символ — строчная латинская буква
четвертый символ — заглавная латинская буква
пятый символ — заглавная латинская буква

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/683127/tests_2833098.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.2/Module_11.2.17

regex = r''

Sample Input 1:
My name is t1mUR and I am a1iVE!
Sample Output 1:
t1mUR a1iVE

Sample Input 2:
I read the l1eTTer
Sample Output 2:
l1eTT

Sample Input 3:
Stood u1pPP
Sample Output 3:
u1pPP
'''
regex = r'[a-z]\d[a-z][A-Z]{2}'