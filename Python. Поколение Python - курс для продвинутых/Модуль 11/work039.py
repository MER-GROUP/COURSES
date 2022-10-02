'''
Хороший пароль
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, 
содержит хотя бы одну цифру, заглавную и строчную букву. 
Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

Формат входных данных
На вход программе подаётся одна строка текста.

Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.

Тестовые данные
Sample Input 1:
abcABC9
Sample Output 1:
YES

Sample Input 2:
abAB34
Sample Output 2:
NO

Sample Input 3:
DFSDFSDFSDsdfjsdfnsm
Sample Output 3:
NO
'''
# Решение
import string
pswd = input()
print(
    'YES' if (
        7 <= len(pswd) 
        and any([i in string.digits for i in pswd])
        and any([i in string.ascii_lowercase for i in pswd])
        and any([i in string.ascii_uppercase for i in pswd])
    ) else 'NO'
)