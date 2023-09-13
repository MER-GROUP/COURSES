'''
Погода

Имеется массив данных за месяц, содержащий информацию о температуре 
воздуха (в градусах Цельсия) и количестве осадков (в мм) за каждый день месяца. 
Необходимо найти дни, в которые было пасмурно, т.е. количество осадков было 
больше среднего значения за месяц, а температура воздуха была ниже средней 
температуры за месяц. Создайте функцию special_days(temperatures, precipitations), 
которая принимает numpy массивы с данными о температуре и количестве осадков 
за каждый день месяца. Функция должна возвращать numpy массив номеров дней, 
которые удовлетворяют условиям задачи.

Sample Input:
-4, 2, 6, 10, 11, 12, 14, 16, 13, 7, 2, -2, -7, -9, -6, 1, 3, 5, 8, 10, 11, 12, 8, 5, -1
12, 9, 10, 6, 5, 7, 8, 14, 16, 17, 18, 12, 9, 7, 8, 6, 5, 4, 3, 2, 4, 7, 9, 10, 12

Sample Output:
1 2 11 12 13 24 25
'''
import numpy as np
from datetime import datetime, timedelta
from dateutil.parser import parse

def special_days(temperatures: np.ndarray, precipitations: np.ndarray) -> np.ndarray:
    arr = np.arange(1, temperatures.size+1)
    return arr[
        (precipitations.mean() < precipitations) &
        (temperatures.mean() > temperatures)
    ]

if __name__ == '__main__':
    temperatures, precipitations = (
        np.array(
            object=input().split(', '),
            dtype=int
        )
        for _ in range(2)
    )
    print(special_days(temperatures, precipitations))