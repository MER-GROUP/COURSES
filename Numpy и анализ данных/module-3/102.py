'''
Интернет-магазин

В базе данных интернет-магазина есть таблица со списком всех товаров и их ценами. Напишите 
функцию return_item(item, old_price, new_price), которая принимает три numpy массива item, old_price, 
new_price, содержащие название товара, старую цену  и новую цену соответственно и возвращает 
строку с товарами, цена на которые снизилась более чем на 20%. Товары разделены пробелами 
и следуют в том же порядке, в котором они находятся в исходном массиве.

Sample Input:
Яблоко, Апельсин, Манго, Банан, Груша, Ананас, Киви, Арбуз, Дыня, Персик, Слива, Абрикос, Мандарин, Грейпфрут, Лимон, Лайм, Виноград, Черешня, Клубника, Малина
50, 60, 100, 40, 70, 150, 80, 200, 120, 90, 80, 70, 65, 80, 55, 60, 90, 100, 120, 130
45, 45, 90, 32, 60, 130, 70, 160, 100, 72, 64, 60, 50, 60, 45, 50, 72, 80, 100, 110

Sample Output:
Апельсин Мандарин Грейпфрут
'''
import numpy as np
from datetime import datetime
from dateutil.parser import parse

def return_item(item, old_price, new_price):
    arr_item_20_percent = old_price * 0.2
    print(arr_item_20_percent) ###
    arr_difference = old_price - new_price
    print(arr_difference) ###
    arr2_less_arr1 = new_price < old_price
    print(arr2_less_arr1) ###

    return (
        item[
            (arr2_less_arr1) &
            (20 < arr_difference)
        ]
    )

if __name__ == '__main__':
    item, old_price, new_price = (
        np.array(
            object=input().split(', '),
            dtype=None
        )
        for _ in range(3)
    )

    print('-----------------------------')
    print(item)
    print('-----------------------------')
    print(old_price)
    print('-----------------------------')
    print(new_price)
    print('-----------------------------')
    print(return_item(item, old_price.astype(int), new_price.astype(int)))