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

sys.stdin = open(file='036.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

pass