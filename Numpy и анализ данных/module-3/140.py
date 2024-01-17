'''
Угадай цвет магического кристалла!

Жил-был один умный волшебник, который любил создавать различные артефакты. 
Однажды он создал магический кристалл, который имел некоторые особенности. 
Каждый день, начиная с первого, кристалл мог менять свой цвет на зеленый. 
Но, если номер дня был кратен трём, то кристалл менял свой цвет на красный. 
Если же номер дня был кратен пяти, то кристалл менял свой цвет на синий. 
Если же номер дня был кратен и трём, и пяти одновременно, то кристалл менял 
свой цвет на жёлтый.

Волшебник хотел узнать, какой цвет у кристалла будет на n-й день его существования. 
Для этого он написал следующее условие: ХХХХ

Затем волшебник использовал функцию np.where для того, чтобы определить цвет 
кристалла на n-й день его существования. Он создал одномерный массив 
длиной n элементов, где каждый элемент представляет собой номер дня, начиная с первого. 
Затем он использовал функцию np.where, чтобы определить цвет кристалла на n-й день.

Таким образом, задача волшебника на использование функции np.where состояла в том, 
чтобы определить цвет магического кристалла на n-й день его существования 
в соответствии с правилами, заданными в условии. И вам нужно сделать то же самое 
и вывести итоговый массив цветов кристалла через пробел в каждый день, начиная 
с первого по n-ый. На вход поступает целое число n, на выход нужно подать требуемый массив.

Sample Input:
20

Sample Output:
['зеленый' 'зеленый' 'красный' 'зеленый' 'синий' 'красный' 'зеленый'
 'зеленый' 'красный' 'синий' 'зеленый' 'красный' 'зеленый' 'зеленый'
 'желтый' 'зеленый' 'зеленый' 'красный' 'зеленый' 'синий']
'''
import numpy as np
from sys import stdin
stdin = open(file='140.csv', mode='rt', encoding='utf-8', newline='')

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

    arr_color = np.array(object=['зеленый' for _ in range(*arr1)], dtype=np.str_)
    arr_index = np.arange(1, *arr1+1)
    # print(arr_color) # test
    # print(arr_index) # test
    arr_color = np.where(0 == arr_index % 3, 'красный', arr_color)
    arr_color = np.where(0 == arr_index % 5, 'синий', arr_color)
    arr_color = np.where(((0 == arr_index % 3) & (0 == arr_index % 5)), 'желтый', arr_color)
    print(arr_color)