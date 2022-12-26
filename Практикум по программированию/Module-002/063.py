'''
Четные числа

Входные данные
Вводятся целые числа a и b. Гарантируется, что a не превосходит b

Выходные данные
Выведите (через пробел) все четные числа от a до b (включительно).

Sample Input:
2
5
Sample Output:
2 4
'''
a, b = (int(input()) for _ in range(2))

print(
    *filter(
        lambda x: 0 == x % 2,
        range(a, b+1)
    )
)

print(*(i for i in range(a, b+1) if 0 == i % 2))