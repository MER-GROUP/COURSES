'''
Функция fib()
Используя синтаксис анонимных функций, реализуйте рекурсивную функцию fib(), 
которая принимает один аргумент:

n — натуральное число

Функция должна возвращать n-ый член последовательности Фибоначчи.

Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел, 
где каждое последующее число является суммой двух предыдущих: 

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию fib(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640036/tests_2669880.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.3/Module_9.3.16

Sample Input 1:
print(fib(1))
Sample Output 1:
1

Sample Input 2:
print(fib(2))
Sample Output 2:
1

Sample Input 3:
print(fib(5))
Sample Output 3:
5
'''
fib = lambda x: 1 if 2 >= x else fib(x-1) + fib(x-2)

if __name__ == '__main__':
    print(fib(1))
    print(fib(2))
    print(fib(5))