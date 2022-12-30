'''
Подсчет чисел
Подсчитайте, сколько среди данных N чисел нулей, положительных чисел, отрицательных чисел.

Входные данные
Вводится число N, а затем N целых чисел.

Выходные данные
Необходимо вывести сначала число нулей, затем число положительных и отрицательных чисел.

Sample Input:
5
28
0
0
0
0
Sample Output:
4 1 0
'''
def counts(arr):
    zero, plus, minus = [0] * 3
    for i in arr:
        if 0 == i:
            zero += 1
        elif 0 < i:
            plus += 1
        else:
            minus += 1
    return zero, plus, minus

arr = (int(input()) for _ in range(int(input())))
print(*counts(arr))