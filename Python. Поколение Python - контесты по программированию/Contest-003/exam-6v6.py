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
    Разбиваем `int_list` на два множества с одинаковыми суммами
    Время работы O(n log n)
    """
    A=list()
    B=list()
    for n in sorted(int_list, reverse=True):
        if sum(A) < sum(B):
           A.append(n)
        else:
           B.append(n)
    return sum(A) == sum(B)

if __name__ == '__main__':
    print(find_partition(map(int, input().split())))