'''
Быстрое возведение в степень
Возводить в степень можно гораздо быстрее, чем за nn умножений. 
Для этого нужно воспользоваться следующими рекуррентными соотношениями:

a^n=(a^2)^{2/n}, при четном n
a^n=a⋅a^{n−1}, при нечетном n

Реализуйте функцию get_fast_pow() с использованием рекурсии, 
которая принимает два аргумента в следующем порядке:

a — положительное целое число
n — неотрицательное целое число

Функция должна вычислять значение a в степени n, используя алгоритм 
быстрого возведения в степень, и возвращать полученный результат.

Примечание 1. При решении не используйте оператор возведения в степень **.

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию get_fast_pow(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2429282.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.11

Sample Input 1:
print(get_fast_pow(2, 10))
Sample Output 1:
1024

Sample Input 2:
print(get_fast_pow(5, 2))
Sample Output 2:
25

Sample Input 3:
print(get_fast_pow(2, 100))
Sample Output 3:
1267650600228229401496703205376
'''
def get_fast_pow(a: int, n: int) -> int:
    def rec(_a: int = n, _n: int = n) -> int:
        if not _n:
            return 1
        elif _n % 2:
            return _a * rec(_a, _n-1)
        else:
            return rec(_a * _a, _n//2)
    return rec(a, n)

if __name__ == '__main__':
    print(get_fast_pow(2, 10))
    print(get_fast_pow(5, 2))
    print(get_fast_pow(2, 100))