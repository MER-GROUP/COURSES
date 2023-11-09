'''
Факториал-конечные-нули

Функция trailing_zeros()

Реализуйте функцию trailing_zeros(), которая принимает один аргумент:

n – неотрицательное целое число (0 ≤ n ≤ 10^9)
Функция должна возвращать количество нулей в конце записи факториала числа n.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую  
функцию trailing_zeros(), но не код, вызывающий ее.

Ограничения:
Ограничение по времени на тест: 2 секунды.

Ограничение по памяти на тест: 32 мб.

Sample Input 1:
print(trailing_zeros(0))
Sample Output 1:
0

Sample Input 2:
print(trailing_zeros(4))
Sample Output 2:
0

Sample Input 3:
print(trailing_zeros(5))
Sample Output 3:
1

Sample Input 4:
print(trailing_zeros(10))
Sample Output 4:
2

Sample Input 5:
print(trailing_zeros(50))
Sample Output 5:
12

Sample Input 6:
print(trailing_zeros(500))
Sample Output 6:
124

Sample Input 7:
print(trailing_zeros(10000))
Sample Output 7:
2499

Sample Input 8:
print(trailing_zeros(10**5 + 1))
Sample Output 8:
24999

Sample Input 9:
print(trailing_zeros(10**6 + 1))
Sample Output 9:
249998

Sample Input 10:
print(trailing_zeros(10**8 + 999))
Sample Output 10:
25000245
'''

'''
Вся сложность задачи заключается в том, что к примеру посчитать число 123456789! 
в явном виде мы не можем, поскольку оно слишком большое. Однако посчитать количество нулей, 
на которые оканчивается это число, можно – для этого вовсе не нужно знать все число целиком.

Напомним, что факториалом числа n называется произведение натуральных чисел от 1 до n, 
другими словами, n! = 1*2*3*...*n. Ноль в конце произведения появляется в результате 
перемножения 2 и 5. Но поскольку при разложении на простые множители числа n! двоек больше, 
чем пятерок, то количество нулей в конце n! равно количеству пятерок в разложении n! 
на простые множители.
'''

def trailing_zeros(n: int) -> int:
    zeros = 0
    while 0 < n:
        n //= 5
        zeros += n
    return zeros

if __name__ == '__main__':
    print(trailing_zeros(0))
    print(trailing_zeros(4))
    print(trailing_zeros(5))
    print(trailing_zeros(10))
    print(trailing_zeros(50))
    print(trailing_zeros(500))
    print(trailing_zeros(10000))
    print(trailing_zeros(10**5 + 1))
    print(trailing_zeros(10**6 + 1))
    print(trailing_zeros(10**8 + 999))