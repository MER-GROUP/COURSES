'''
Анна и камни

Однажды в лесу жила прекрасная принцесса по имени Анна, у которой был ящик 
с самыми красивыми и драгоценными камнями. Она очень любила свои камни и хранила 
их с большой осторожностью. Однажды у нее появилось много новых камней, 
но она заметила, что некоторые из них не так яркие и блестящие, как она хотела бы. 
Чтобы узнать, какие из камней ей не нравятся, Анна решила использовать функцию np.where.

Она решила, что если яркость камня меньше  51, то это камень, который ей не нравится, 
и она должна его выбросить. Для этого она написала условие в виде "если яркость камня 
меньше 51, то он не подходит для моей коллекции". Затем она использовала 
функцию np.where для того, чтобы найти номера всех камней, которые ей не нравятся, 
и выбросить их из своей коллекции.

Таким образом, задача принцессы Анны на использование функции np.where состояла 
чтобы вывести на экран яркости всех камней, которые она оставила в своей коллекции.

Sample Input:
88 51 18 92 50 74 72 20 67 97 86 90

Sample Output:
88 51 92 74 72 67 97 86 90
'''
import numpy as np
from sys import stdin
stdin = open(file='139.csv', mode='rt', encoding='utf-8', newline='')

if __name__ == '__main__':
#     arr = np.fromstring(
#         string=stdin.read(),
#         # dtype=int,
#         dtype=float,
#         sep = ' '
#     )
#     print(arr) # test #
#     print(type(arr)) # test #

    # arr1, arr2, arr3, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # print(arr1, arr2, arr3, sep='\n')

    # arr1, arr2, *_ = (np.array(object=i.split(), dtype=str) for i in stdin)
    # arr1, arr2, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    arr1, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    print(arr1) # test
    # print(arr2) # test

    print(*arr1[np.where(50 < arr1)])
    # print(*arr1[np.where(50 < arr1, True, False)])