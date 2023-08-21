'''
База данных

В базе данных интернет-магазина есть таблица со списком всех заказов и информацией о том, 
был ли заказ оплачен. Напишите программу на Python с использованием библиотеки numpy, 
которая находит все заказы, которые еще не были оплачены.

На вход поступает строка целых чисел, содержащая id заказа, и строка состоящая из слов True False, 
разделенных пробелом. True означает, что соответствующий заказ был оплачен, False - не был оплачен. 

Sample Input:
1000 1001 1002 1003 1004 1005 1006 1007 1008 1009 1010 1011 1012 1013 1014 1015 1016 1017 1018 1019
False False True False False False False False False True True False True True False True False True False True

Sample Output:
[1000 1001 1003 1004 1005 1006 1007 1008 1011 1014 1016 1018]
'''
import numpy as np

if __name__ == '__main__':
    arr1 = np.fromstring(string=input(), dtype=int, sep=' ')
    arr2 = np.array(object=['True'==i for i in input().split()], dtype=bool)
    print(arr1[~arr2])