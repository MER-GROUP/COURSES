'''
Функция tribonacci()
Последовательность Трибоначчи – последовательность натуральных чисел, 
где каждое последующее число является суммой трех предыдущих:

1,1, 1, 3, 5, 9, 17, 31, 57, 105 …

Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, 
которая принимает один аргумент:

n — натуральное число

Функция должна возвращать n-й член последовательности Трибоначчи.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию tribonacci(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2429571.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.14

Sample Input 1:
print(tribonacci(1))
Sample Output 1:
1

Sample Input 2:
print(tribonacci(7))
Sample Output 2:
17

Sample Input 3:
print(tribonacci(4))
Sample Output 3:
3
'''
# # без мемоизации
# def tribonacci(n: int) -> int:
#     def rec(num: int = n) -> int:
#         if num in (1, 2, 3):
#             return 1
#         else:
#             return rec(num-1) + rec(num-2) + rec(num-3)
#     return rec(n)

# с мемоизацией
def tribonacci(n: int) -> int:
    _cache = {1: 1, 2: 1, 3: 1}

    def rec(num: int = n) -> int:
        _tribonacci_n = _cache.get(num)
        if _tribonacci_n is None:
            _tribonacci_n = rec(num-1) + rec(num-2) + rec(num-3)
            _cache[num] = _tribonacci_n
        return _tribonacci_n
    
    return rec(n)

if __name__ == '__main__':
    print(tribonacci(1))
    print(tribonacci(7))
    print(tribonacci(4))