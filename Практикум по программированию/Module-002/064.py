'''
Остаток

Входные данные
Вводятся 4 числа: a, b, c и d. 

Выходные данные
Выведите все числа на отрезке от a до b, 
дающие остаток c при делении на d. 
Если таких чисел не существует, 
то ничего выводить не нужно.

Sample Input:
2
5
0
2
Sample Output:
2 4
'''
a, b, c, d = (int(input()) for _ in range(4))

print(
    *filter(
        lambda x: c == x % d,
        range(a, b)
    )
)

print(*(i for i in range(a, b) if c == i % d))