'''
Функция print_digits() 2 😎
Реализуйте функцию print_digits() с использованием рекурсии, 
которая принимает один аргумент:

number — натуральное число

Функция должна выводить все цифры числа number, 
начиная со старших разрядов, каждое на отдельной строке.

Примечание 1. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию print_digits(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/637962/tests_3110917.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.2/Module_8.2.13

Sample Input 1:
print_digits(12345)
Sample Output 1:
1
2
3
4
5

Sample Input 2:
print_digits(2077)
Sample Output 2:
2
0
7
7

Sample Input 3:
print_digits(8)
Sample Output 3:
8
'''
def print_digits(number: int) -> None:
    def rec(n: int = number) -> None:
        if 0 < n:
            a, b = divmod(n, 10)
            rec(a)
            print(b)
    rec(number)

if __name__ == '__main__':
    print_digits(2077)