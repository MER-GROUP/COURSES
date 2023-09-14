'''
Последовательность символов

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное 
выражение, которому соответствуют последовательности символов формата Xxxxx, 
где X — любая буква латинского алфавита в произвольном регистре, а x — произвольная цифра.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/683127/tests_2834152.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.2/Module_11.2.16

regex = r''

Sample Input 1:
Order 1: B938274, Order 2: T8372, Order 3: g883929
Sample Output 1:
B9382 T8372 g8839

Sample Input 2:
is valid number A123(-), a123(-), B12345(+), b12345(+)
Sample Output 2:
B1234 b1234

Sample Input 3:
check 123A123, - 5739bb1234b4 -, BOM999_19
Sample Output 3:
b1234
'''
regex = r'[A-Za-z]\d{4}'