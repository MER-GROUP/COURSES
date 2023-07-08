'''
slice-7

На вход поступает две строки, содержащие одинаковое количество целых чисел, 
разделенных пробелом. На их основе создать список numpy, состоящий из элементов, 
которые находятся на четных позициях первого списка, затем следуют элементы, 
стоящие на нечетных позициях второго списка. Если длина списков нечетная, 
то последний элемент не учитывается. Полученный список вывести на экран.

Sample Input:
5 21 7 29 25 25 13 6 30 23
23 63 34 5 66 81 81 31 3 83
Sample Output:
[ 5  7 25 13 30 63  5 81 31 83]

Sample Input:
27 22 24 1 26 20 6 14 31 7 31
83 92 1 49 43 45 78 6 27 33 27
Sample Output:
[27 24 26  6 31 92 49 45  6 33]
'''
import numpy as np

if __name__ == '__main__':
    a = np.fromstring(string=input(), dtype=int, sep=' ')
    b = np.fromstring(string=input(), dtype=int, sep=' ')
    if a.size % 2: a.resize(a.size-1)
    if b.size % 2: b.resize(b.size-1)
    # c = np.concatenate((a[::2], b[1::2]), dtype=int)
    c = np.concatenate((a[::2], b[1::2]))
    if c.size % 2: c.resize(c.size-1)
    print(c)