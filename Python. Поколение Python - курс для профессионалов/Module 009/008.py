'''
Функция my_pow()
Реализуйте функцию my_pow(), которая принимает один аргумент:

number — целое неотрицательное число

Функция должна возвращать сумму, состоящую из цифр числа, 
возведенных в степень их порядкового номера.

Примечание 1. Рассмотрим число 139 из первого теста. 
Сумма цифр этого числа, возведенных в степень их порядкового номера, равна:
1^1 + 3^2 + 9^3 = 739

Примечание 2. В задаче удобно воспользоваться функциями enumerate() и sum().

Примечание 3. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию my_pow(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640035/tests_2642895.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.1/Module_9.1.13

Sample Input 1:
print(my_pow(139))
Sample Output 1:
739

Sample Input 2:
print(my_pow(123))
Sample Output 2:
32

Sample Input 3:
print(my_pow(0))
Sample Output 3:
0
'''
# cycle
def my_pow(number: int) -> int:
    return sum(num**n for n,num in enumerate([int(i) for i in str(number)], start=1))

# recursive
def my_pow(number: int) -> int:
    _n = len(str(number))
    def rec(num: int = number, n: int = _n):
        if not n:
            return 0
        else:
            return (num % 10)**n + rec(num // 10, n - 1)
    return rec(number)

if __name__ == '__main__':
    print(my_pow(139))
    print(my_pow(123))
    print(my_pow(0))