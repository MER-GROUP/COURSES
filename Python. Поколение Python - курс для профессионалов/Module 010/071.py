'''
Книга по математике

Тимур пришел в книжный магазин, чтобы приобрести новую книгу по математике, стоимость 
которой равна 100$. У него в кошельке имеется множество купюр различного номинала, 
которые представлены в списке wallet. Например, Тимур может расплатиться одной 
купюрой в 100$ или двумя по 50$.

Дополните приведенный ниже код, чтобы он вывел количество способов, которыми 
Тимур может приобрести книгу стоимостью 100$.

Примечание. Способы расплатиться наборами купюр вида 50, 20, 20, 10 и 20, 10, 50, 20 
считаются одинаковыми и не должны учитываться повторно.

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

if __name__ == '__main__':
    wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

    n = len(wallet)
    # n = 2
    c = 0
    while n:
        combinations = it.combinations(wallet, n)
        combinations_sort = map(sorted, combinations)
        combinations_tuple = map(tuple, combinations)
        # print('----------------') #####
        # print(*combinations_sort) #####
        # print('----------------') #####
        # print(*combinations_tuple) #####
        combinations_set = set(combinations_tuple)
        # print('----------------') #####
        # print(combinations_set) #####

        for el in combinations_set:
            if 100 == sum(el):
                c += 1

        n -= 1

    print(c)