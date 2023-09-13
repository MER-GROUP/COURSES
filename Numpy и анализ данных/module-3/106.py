'''
Магазины

Имеется массив данных, содержащий информацию о ценах на продукты 
в нескольких магазинах. Необходимо найти все продукты, цена которых 
меньше 10 рублей и при этом в наличии есть не менее 6 единиц товара. 
Для этого создать функцию find_less_10(items, prices, quantities), 
принимающую на вход три numpy массива: items - названия продуктов, 
prices - цены на продукты, quantities - количество оставшихся единиц. 
Функция должна возвращать numpy массив, содержащий названия продуктов, 
соответствующих условиям задачи.

Sample Input:
хлеб, молоко, сыр, яблоки, бананы, колбаса, яйца, сок, кефир, курица
8, 12, 6, 5, 11, 9, 10, 7, 4, 15
10, 2, 8, 6, 4, 7, 3, 9, 5, 12

Sample Output:
хлеб сыр яблоки колбаса сок
'''
import numpy as np
from datetime import datetime, timedelta
from dateutil.parser import parse

def find_less_10(items: np, prices: np, quantities: np) -> np:
    return items[(10>prices.astype(int)) & (6<=quantities.astype(int))]

if __name__ == '__main__':
    items, prices, quantities = (
        np.array(
            object=input().split(', '),
            dtype=None
        )
        for _ in range(3)
    )
    print(find_less_10(items, prices, quantities))