'''
Задача о красном и зеленом драконах

Два дракона, красный и зеленый, соревнуются между собой, совершая различные трюки. 
Красный дракон совершает n трюка в день и получает за каждый трюк m очков. 
Зеленый дракон совершает i трюков в день и получает за каждый трюк j очков. 
Кто из драконов наберет больше очков за N дней? 

На вход поступает 5 чисел в одной строке через пробел: n, m, i, j, N. 

В качестве ответа необходимо вывести слово "зеленый", "красный" или "ничья" 
без кавычек. Необходимо воспользоваться возможностями библиотеки numpy 
для решения данной задачи.

Sample Input:
3 5 5 3 10
Sample Output:
ничья
'''
import numpy as np

if __name__ == '__main__':
    arr = np.fromstring(string=input(), dtype=None, sep=' ')
    red = arr[0] * arr[1] * arr[-1]
    green = arr[2] * arr[3] * arr[-1]
    print((('красный', 'ничья')[int(red == green)], 'зеленый')[int(red < green)])