'''
Итератор PowerOf
Реализуйте класс PowerOf, порождающий итераторы, конструктор которого 
принимает один аргумент:

number — ненулевое число

Итератор класса PowerOf должен генерировать бесконечную последовательность 
целых неотрицательных степеней числа number в порядке возрастания, начиная с нулевой степени.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимый класс PowerOf.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2771338.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.11

Sample Input:
power_of_two = PowerOf(2)
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
Sample Output:
1
2
4
8
'''
class PowerOf:
    def __init__(self, number: int) -> None:
        self.number = number
        self.digit = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.digit += 1
        return self.number**(self.digit-1)

if __name__ == '__main__':
    power_of_two = PowerOf(2)
    print(next(power_of_two))
    print(next(power_of_two))
    print(next(power_of_two))
    print(next(power_of_two))

# import functools, time

# def timer(iters=10):
#     def decorator(func):   
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.perf_counter()
#                 value = func(*args, **kwargs)
#                 end = time.perf_counter()
#                 total += end - start
#             print(f'Среднее время выполнения {func.__name__}: {round(total/iters, 4)} сек.')
#             return value
#         return wrapper
#     return decorator

# class PowerOfWithMemo:
#     def __init__(self, number: int):
#         self.num = number
#         self.index = -1
#         self.__next__.__dict__[0] = 1

#     def __next__(self):
#         self.index += 1
#         if self.index == 0:
#             return self.__next__.__dict__[0]
#         val = self.__next__.__dict__[self.index] = self.__next__.__dict__[self.index - 1] * self.num
#         return val

#     def __iter__(self):
#         return self

# class PowerOfSimple:
#     def __init__(self, number):
#         self.cache = 1
#         self.number = number

#     def __iter__(self):
#         return self

#     def __next__(self):
#         val = self.cache
#         self.cache *= self.number
#         return val

# @timer()
# def test_with_memo(n):
#     power_of_2 = PowerOfWithMemo(2)
#     res = [next(power_of_2) for _ in range(n)]

# @timer()
# def test_simple(n):
#     power_of_2 = PowerOfSimple(2)
#     res = [next(power_of_2) for _ in range(n)]

# print(test_with_memo(10000))
# print(test_simple(10000))