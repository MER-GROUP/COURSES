'''
Анализ трат клиентов в интернет-магазине

Вы работаете в компании, которая занимается анализом данных. Ваша задача - провести 
анализ трат клиентов в интернет-магазине и определить, какие категории товаров наиболее 
популярны среди клиентов с разными уровнями дохода. У вас есть два одномерных 
массива: income_levels поступает в первой строке и spending_categoriesпоступает 
во второй строке. Массив income_levels содержит информацию о доходе клиентов, 
а массив spending_categories содержит информацию о том, в каких категориях 
товаров тратят больше всего денег клиенты с соответствующим уровнем дохода.

Ваша задача - определить, в каких категориях товаров тратят деньги клиенты 
с высоким уровнем дохода, а в каких категориях товаров тратят деньги с низким 
уровнем дохода. Пороговым значением уровня дохода считать доход, превышающий 60000 рублей.

На выход подать два массива через пробел, первый массив - названия категорий 
товаров, которые наиболее популярны среди клиентов с высоким уровнем доходов 
и среди клиентов с низким уровнем доходов. Название категорий должно следовать 
в том же порядке в котором они идут в исходном массиве.

Sample Input:
15000 20000 25000 30000 40000 50000 60000 70000 90000 120000 200000
еда одежда электроника книги еда одежда образование еда одежда путешествия украшения

Sample Output:
['еда' 'одежда' 'путешествия' 'украшения'] ['еда' 'одежда' 'электроника' 'книги' 'еда' 'одежда' 'образование']
'''
import numpy as np
from sys import stdin
stdin = open(file='138.csv', mode='rt', encoding='utf-8', newline='')

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

    arr1, arr2, *_ = (np.array(object=i.split(), dtype=str) for i in stdin)
    # arr1, arr2, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # arr1, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    print(arr1) # test
    print(arr2) # test

    limit = 60000
    # mask_limit = arr1.astype(dtype=int)[arr1.astype(dtype=int)<limit]
    mask_limit = np.where(arr1.astype(dtype=int)<=limit, True, False)
    # print(~mask_limit) # test
    # print(mask_limit) # test
    print(arr2[~mask_limit], arr2[mask_limit])