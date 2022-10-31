'''
Возрастающая подпоследовательность
Дана последовательность натуральных чисел. Напишите программу, 
которая из данной последовательности вычеркивает минимальное 
количество чисел так, чтобы оставшиеся шли в порядке возрастания.

Формат входных данных
На вход программе подается последовательность натуральных чисел, 
разделенных пробелом. Количество чисел в последовательности не превышает 10000.

Формат выходных данных
Программа должна из введенной последовательности вычеркнуть 
минимальное количество чисел так, чтобы оставшиеся шли в 
порядке возрастания. Не вычеркнутые числа следует вывести 
через пробел, сохранив их исходный порядок следования.  

Примечание 1. Если вариантов вычеркнуть числа несколько, можно вывести любой.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/718107/tests_3019847.zip

tests

Sample Input 1:
2 5 3 4 6 1
Sample Output 1:
2 3 4 6

Sample Input 2:
1 3 5 2 4
Sample Output 2:
1 2 4

Sample Input 3:
5
Sample Output 3:
5
'''
# Решение
def subsequence(seq):
    if not seq:
        return seq

    # offset by 1 (j -> j-1)
    M = [None] * len(seq)    
    P = [None] * len(seq)

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    # the first element.
    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search: we want the largest j <= L
        # such that seq[M[j]] < seq[i] (default j = 0),
        # hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            # this will also set the default value to 0
            j = lower 

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    # reversing
    return result[::-1]    

if __name__ == '__main__':
    print(*subsequence(list(map(int, input().split()))))