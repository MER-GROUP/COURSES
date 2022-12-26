'''
Високосный год
Напишите программу, которая определяет, является ли год високосным.

Формат входных данных
На вход программе в первой строке подается целое число n, 
в последующих n строках вводятся натуральные числа, представляющие года.

Формат выходных данных
Программа должна для каждого введенного года вывести True, 
если он является високосным, или False в противном случае.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/570049/tests_2580724.zip

Sample Input 1:
1
2021
Sample Output 1:
False

Sample Input 2:
4
1999
2000
2001
2002
Sample Output 2:
False
True
False
False

Sample Input 3:
3
4433
2048
9757
Sample Output 3:
False
True
False
'''
from calendar import isleap

years = (int(input()) for _ in range(int(input())))
print(
    *[
        (False, True)[isleap(year)] for year in years
    ],
    sep='\n'
)