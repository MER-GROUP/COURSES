'''
Одинаковые суммы
Напишите программу, которая проверяет, возможно ли разбить данный набор чисел на два непустых набора с одинаковой суммой.

Формат входных данных
На вход программе последовательность натуральных чисел, разделенных пробелом, которые представляют исходный набор. Количество чисел в последовательности не превышает 10000.

Формат выходных данных
Программа должна вывести True, если введенный набор чисел возможно разбить на два непустых набора с одинаковой суммой, или False в противном случае.

Примечание 1. При разбиении должны быть использованы все числа исходного набора.

Примечание 2. Рассмотрим первый тест. Имеем следующий исходный набор чисел:
1,2,3,4,6

Данный набор можно разбить на два следующих набора:
1,3,4 и 2,6

Оба набора имеют одинаковую сумму, равную 8.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/718107/tests_3019844.zip

Sample Input 1:
1 2 3 4 6
Sample Output 1:
True

Sample Input 2:
4 6
Sample Output 2:
False

Sample Input 3:
4 2 5 2 7 3 9 3 6 2 3 43 1 44 123 1
Sample Output 3:
True
'''
# Решение
def find_partition(int_list):
    """
    Использование множества set()
    Время работы O(n log n)
    """
    n = sum(int_list)
    if n % 2 == 1:
        return False
    elif max(int_list) > n // 2:
        return False
    elif n // 2 in int_list:
        return True
    elif len(int_list) < 2:
        return False
    else:
        possible_sums = set()
        for num in int_list:
            sums_to_add = set()
            for s in possible_sums:
                if (s + num) not in possible_sums:
                    sums_to_add.add(s+num)
                    if s + num == n // 2:
                        return True
            possible_sums.add(num)
            possible_sums.update(sums_to_add)
        return False

if __name__ == '__main__':
    print(find_partition(list(map(int, input().split()))))