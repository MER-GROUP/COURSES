'''
Сумма чисел

Напишите программу, которая складывает все натуральные числа в строке, 
находящиеся в указанном диапазоне индексов.

Формат входных данных
На вход программе сначала подаются два целых числа aa и b, больших или 
равных 0, разделенные пробелом, а затем — строка.

Формат выходных данных
Программа должна вывести сумму всех натуральных чисел в введенной строке, 
находящихся в диапазоне индексов от a (включительно) до b (не включительно). 
Если в указанном диапазоне нет ни одного числа, программа должна вывести 0.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/699083/tests_2916589.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.9/Module_11.9.19

Sample Input 1:
0 5
11:20 a.m. - 12:00 p.m
Sample Output 1:
31

Sample Input 2:
0 10
Нет ни одного числа в этой строке
Sample Output 2:
0

Sample Input 3:
0 100
Нет ни одного числа в этой строке
Sample Output 3:
0
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def func(string: str, text: str) -> int:
    a, b = map(int, string.split())
    pattern_compile = re.compile(fr'\d+')
    match = pattern_compile.findall(text, pos=a, endpos=b)
    return sum(
        map(
            int,
            match
        ),
        0
    )

if __name__ == '__main__':
    # stdin = open(file='063-test.csv', mode='rt', encoding='utf-8', newline='')
    # # sentense = map(str, stdin)
    # sentense = stdin.read()
    # print(sentense) # test
    # print('------') # test
    # pattern = rf''

    print(func(input(), input()))