'''
Комментатор
Дан блок кода на языке Python. Напишите программу, 
которая определяет количество строк в данном коде, 
которые содержат в себе только комментарии. 
Если в строке помимо комментария имеется что-то еще, 
то такую строку учитывать не нужно.

Формат входных данных
На вход программе подается произвольное количество строк, 
в совокупности представляющих блок кода на языке Python.

Формат выходных данных
Программа должна вывести единственное число — количество строк 
в введенном коде, которые содержат в себе только комментарии.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/520159/tests_2534820.zip

Sample Input:
s = str(input())
k = 0
#подсчитываем количество цифр
for i in range(len(s)):
    #проверяем каждый символ
    if s[i] in '0123456789': #проверяем, является ли элемент строки цифрой
        k += 1
print(k)
Sample Output:
2
'''
import sys

print(
    sum(
        map(
            lambda x: x.strip().startswith('#'),
            sys.stdin,
        )
    )
)