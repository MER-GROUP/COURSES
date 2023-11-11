'''
Сумма цифр
Напишите программу с использованием рекурсии, которая принимает 
на вход число и выводит сумму цифр этого числа.

Формат входных данных
На вход программе подается неотрицательное целое число.

Формат выходных данных
Программа должна определить сумму цифр введенного числа 
и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2429572.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.7

Sample Input 1:
25
Sample Output 1:
7

Sample Input 2:
10000
Sample Output 2:
1

Sample Input 3:
12345
Sample Output 3:
15
'''
def sum_digits(n: int) -> int:
    def rec(num: int = n) -> int:
        if not num // 10:
            return num % 10
        else:
            return (num % 10) + rec(num // 10)
    return rec(n)

if __name__ == '__main__':
    print(sum_digits(int(input())))