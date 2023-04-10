'''
Обычное возведение в степень
Реализуйте функцию get_pow() с использованием рекурсии, которая принимает 
два аргумента в следующем порядке:

a — положительное целое число
n — неотрицательное целое число

Функция должна вычислять значение a в степени n и возвращать полученный результат.

Примечание 1. При решении не используйте оператор возведения в степень **.

Примечание 2. Для построения рекурсивного алгоритма воспользуйтесь следующим 
рекуррентным соотношением:

a^n = a * a^{n - 1}
 
Примечание 3. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию get_pow(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2429281.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.10

Sample Input 1:
print(get_pow(5, 2))
Sample Output 1:
25

Sample Input 2:
print(get_pow(99, 0))
Sample Output 2:
1

Sample Input 3:
print(get_pow(2, 10))
Sample Output 3:
1024
'''
def get_pow(a: int, n: int) -> int:
    def rec(_a: int = a, _n: int = n) -> int:
        if not _n:
            return 1
        return _a * rec(_a, _n-1)
    return rec(a, n)

if __name__ == '__main__':
    print(get_pow(5, 2))
    print(get_pow(99, 0))