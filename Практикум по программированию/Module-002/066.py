'''
Минимальный делитель
Найдите самый маленький натуральный делитель числа x, 
отличный от 1 (2 <= x <= 30000).

Входные данные
Вводится натуральное число x.

Выходные данные
Выведите наименьший делитель числа x, отличный от 1.

Sample Input:
6
Sample Output:
2
'''
n = int(input())
my_set = set()
# for i in range(2, n+1):
for i in range(2, n//2):
    if not n % i:
        my_set.add(i)
        break
print(min(my_set) if my_set else n)