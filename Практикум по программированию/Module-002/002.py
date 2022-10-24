'''
Следующее и предыдущее
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере. Пробелы, знаки препинания, заглавные и строчные буквы важны!

Входные данные
Вводится целое число, по модулю не превосходящее 10000.

Выходные данные
Выведите сначала фразу "The next number for the number ", затем введенное число, затем слово " is ", окруженное пробелами, затем формулу для следующего за введенным числа, наконец, знак точки без пробела. Аналогично в следующей строке для предыдущего числа.
'''
'''
Tests:

Sample Input:
179
Sample Output:
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
'''
n = int(input())
print(f'The next number for the number {n} is {n + 1}.')
print(f'The previous number for the number {n} is {n - 1}.')

print(f'''
The next number for the number {(n:=int(input()))} is {n+1}.
The previous number for the number {n} is {n-1}.''')