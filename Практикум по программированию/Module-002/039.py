'''
Мороженое
В кафе мороженое продают по три шарика и по пять шариков. 
Можно ли купить ровно k шариков мороженого?

Входные данные
Вводится число k (целое, положительное)

Выходные данные
Программа должна вывести слово YES, 
если при таких условиях можно набрать ровно k шариков (не больше и не меньше), 
в противном случае - вывести NO.

Sample Input:
8
Sample Output:
YES
'''
k = int(input())
mod_3 = k % 3
mod_5 = k % 5
# print(f'mod_3 = {mod_3}')
# print(f'mod_5 = {mod_5}')

if (k in (0, 1, 2)):
    print('NO')
# elif (mod_3 in (0, 1, 2, 3) and mod_5 in (0, 1, 2, 3)):
elif (mod_3 in (0, 2, 3) and mod_5 in (0, 1, 3, 4)) and 1 == len(str(k)):
    print('YES')
elif (mod_3 in (0, 1, 2) and mod_5 in (0, 1, 2, 3, 4)) and 1 < len(str(k)):
    print('YES')
else:
    print('NO')

# k = int(input())
# print('YES' if k not in [1,2,4,7] else 'NO')