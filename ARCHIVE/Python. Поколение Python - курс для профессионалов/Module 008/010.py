'''
Количество цифр
Напишите программу с использованием рекурсии, которая принимает 
на вход число и выводит количество цифр в этом числе.

Формат входных данных
На вход программе подается неотрицательное целое число.

Формат выходных данных
Программа должна определить количество цифр в введенном 
числе и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылкам:
Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2429573.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.6

Sample Input 1:
50
Sample Output 1:
2

Sample Input 2:
17488
Sample Output 2:
5

Sample Input 3:
7
Sample Output 3:
1
'''
def counts(n: str) -> int:
    def rec(num: int = n):
        if not num:
            return 0
        else:
            return 1 + rec(num[1:])
    return rec()

if __name__ == '__main__':
    print(counts(input()))