'''
Интересный перевод
На планете Роботов очень не любят десятичную систему счисления, 
поэтому они попросили Вас написать программу, которая заменяет все встречающиеся 
в тексте числа на эти же числа, но в двоичной системе счисления.

Входные данные
Единственная строка, состоящая из любых символов. Длина строки не превышает 255 символов. 
Гарантируется, что во всех числах нет ведущих нулей.

Выходные данные
Выведите преобразованную строку.

Sample Input:
6^&678JKjdkdl;?.,lk879Pk1kdfl4839
Sample Output:
110^&1010100110JKjdkdl;?.,lk1101101111Pk1kdfl1001011100111
'''
import sys

# sys.stdin = open(file='025.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

# print(bin(1))
# print(bin(1)[2:])

arr_res = list()
for i, el in enumerate(arr):
    if 0 == i:
        arr_res.append(el)
    elif el.isdigit():
        if arr_res[-1].isdigit():
            arr_res[-1] += el
        else:
            arr_res.append(el)
    else:
        arr_res.append(el)

for el in arr_res:
    if el.isdigit():
        print(bin(int(el))[2:], end='')
    else:
        print(el, end='')

print()