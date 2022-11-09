'''
Функция get_biggest() 🌶️🌶️
Реализуйте функцию get_biggest(), которая принимает один аргумент:

numbers — список целых неотрицательных чисел
Функция должна возвращать наибольшее число, которое можно составить 
из чисел из списка numbers. Если список numbers пуст, функция должна вернуть число: -1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], 
из которых можно составить следующие числа:

123, 132, 213, 231, 312, 321

Наибольшим из представленных является 321.

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию get_biggest(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569748/tests_2310080.zip

Sample Input 1:
print(get_biggest([1, 2, 3]))
Sample Output 1:
321

Sample Input 2:
print(get_biggest([61, 228, 9, 3, 11]))
Sample Output 2:
961322811

Sample Input 3:
print(get_biggest([7, 71, 72]))
Sample Output 3:
77271

Sample Input 4:
print(get_biggest([]))
Sample Output 4:
-1
'''
import itertools as it

# # медленный алгоритм на больших данных
# def get_biggest(numbers: list) -> int:
#     if (0 == len(numbers)):
#         return -1
#     else:
#         arr = map(
#             lambda x: int(''.join([str(i) for i in x])),
#             it.permutations(numbers)
#         )
#         # print(*arr)
#         return max(arr)

'''
Алгоритм:
numbers = [9, 95, 982]
Такое будет число на выходе: 9_982_95
Максимальная длина самого большого числа 982 =  3
Изменяем список, умножив строковое представление числа на Максимальную длину:
'9' * 3 = '999'
'95' * 3 = '959595'
'982' * 3 = '982982982'
Сортируем полученные символьные числа лексиграфически по убыванию:
необходимо помнить, как символьно сравниваются строки
'999' >  '959595' 
'982982982' >  '959595'
'999' > '982982982'
Это и есть ключ сортировки: key=lambda x: str(x) * amount_dig_max_el
'''

def get_biggest(numbers: list) -> int:
    if (0 == len(numbers)):
        return -1
    else:
        max_num = max(numbers)
        max_len_num = len(str(max_num))
        arr_str = list(map(str, numbers))
        arr_res = sorted(
            arr_str,
            reverse=True,
            key=lambda x: x * max_len_num
        )
        # print(arr_res)
        return ''.join(arr_res) if int(''.join(arr_res)) else 0

if __name__ == '__main__':

    print(get_biggest([1, 2, 3]))
    print(get_biggest([61, 228, 9, 3, 11]))
    print(get_biggest([7, 71, 72]))
    print(get_biggest([]))
    print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
    # 78554656558534233433222211311
    print(get_biggest([0, 0, 0, 0, 0, 0]))
    # 0