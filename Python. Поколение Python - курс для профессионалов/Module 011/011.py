'''
Последовательность символов 4

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности символов длины 6, удовлетворяющие следующим условиям:

первый символ — цифра 1, 2 или 3
второй символ — цифра 0, 1 или 2
третий символ — цифра 1, 2 или строчная латинская буква x
четвертый символ — цифра 0, 3 или латинская буква a в любом регистре
пятый символ — строчная латинская буква x, s или u
шестой символ — точка или запятая

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/683127/tests_2833100.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.2/Module_11.2.19

regex = r''

Sample Input 1:
I got two strange combinations: 22xAu, 1010x.
Sample Output 1:
22xAu, 1010x.

Sample Input 2:
_010x. A010x, 4010s. 1010s, 010u. '010u,
Sample Output 2:
1010s,

Sample Input 3:
0xAx. \0x3x, 1230xAs. --0xas, 90xAu. *0xau,
Sample Output 3:
30xAs.
'''
regex = r'[1-3][0-2][12x][03Aa][xsu][.,]'