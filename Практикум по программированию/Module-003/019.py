'''
Конвертирование
Дана строка S, в которой выделили подстроку, 
состоящую из символов с i-го по j-й включительно 
(символы строки S нумеруются с единицы) 
и поменяли местами i-й символ с j-м, (i+1)-й с (j-1)-м 
и так далее (конвертировали подстроку). 
Выведите строку S после внесенных изменений.

Входные данные
В первой строке входного файла содержится строка S, 
длиной не более 1000 символов, во второй – числа i и  j (i ≤  j).

Выходные данные
В выходной файл выведите ответ на задачу.

Sample Input:
vjhoamkts
7 8
Sample Output:
vjhoamtks
'''
import sys

# sys.stdin = open(file='019.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(
    map(
        str.strip,
        sys.stdin.readlines()
    )
)
# print(arr) # test

start = arr[0][:int(arr[1].split()[0])-1]
center = arr[0][int(arr[1].split()[0])-1 : int(arr[1].split()[1])][::-1]
end = arr[0][int(arr[1].split()[1]):]
print(start + center + end)