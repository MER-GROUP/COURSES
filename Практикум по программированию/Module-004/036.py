'''
Самое частое число
Дан список. Не изменяя его и не используя дополнительные списки, 
определите, какое число в этом списке встречается чаще всего.

Если таких чисел несколько, выведите любое из них.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 3 2 3 3
Sample Output:
3
'''
import sys
from array import array
from collections import Counter, defaultdict

# sys.stdin = open(file='036.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

print(Counter(arr).most_common()[0][0]) # 1

# 2
_dict = dict()
for _el in arr:
    _dict[_el] = _dict.get(_el, 0) + 1
print(max(_dict, key=_dict.get))

# 3
_defaultdict = defaultdict(int)
for _el in arr:
    _defaultdict[_el] += 1
print(max(_dict, key=_defaultdict.get))

# 4
_max = float('-inf')
_number = int()
for _el in arr:
    if _max < arr.count(_el):
        _max = arr.count(_el)
        _number = _el
print(_el)