'''
Шарики
В одной компьютерной игре игрок выставляет в линию шарики разных цветов. 
Когда образуется непрерывная цепочка из трех и более шариков одного цвета, 
она удаляется из линии. Все шарики при этом сдвигаются друг к другу, 
и ситуация может повториться.

Напишите программу, которая по данной ситуации определяет, сколько шариков 
будет "уничтожено". Естественно, непрерывных цепочек из трех и более 
одноцветных шаров в начальный момент может быть не более одной.

Входные данные
Сначала вводится количество шариков в цепочке (не более 1000) и 
цвета шариков (от 0 до 9, каждому цвету соответствует свое целое число).

Выходные данные
Требуется вывести количество шариков, которое будет "уничтожено".

Sample Input:
5 1 3 3 3 2
Sample Output:
3
'''
import sys
from array import array

sys.stdin = open(file='015.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split()[1:])))
print(arr) # test

_count = int()
_exit = False
_left = 2
while _left<len(arr):
    if arr[_left-2] == arr[_left-1] == arr[_left]:
        _right = _left-2
        while _right<len(arr)-1:
            if arr[_right] == arr[_right+1]:
                _count += 1
                del arr[_right]
                continue
            else:
                _count += 1
                _exit = True
                del arr[_right]
                print('arr[_right] =', arr[_right]) ### test
                if 1 <= _right and arr[_right-1] == arr[_right]:
                    _exit = False
                    while True:
                        if 1 <= _right and arr[_right-1] == arr[_right]:
                            _right -= 1
                        else:
                            _right -= 1
                            _left = _right
                            break
                break
            _right += 1
    if _exit: 
        print('_exit =', arr[_left]) ### test
        break
    _left += 1
print(arr) # test
print(_count)