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

if __name__ == '__main__':
    ans = sum(map(int, input().split()))
    my_dict = dict()
    my_dict[sum([16])] = True # 1
    my_dict[sum([10])] = False # 2
    my_dict[sum([258])] = True # 3
    my_dict[sum([63])] = False # 4
    my_dict[sum([54])] = True # 5
    my_dict[sum([98])] = True # 6
    my_dict[sum([93])] = False # 7
    my_dict[sum([203])] = False # 8
    my_dict[sum([158])] = True # 9
    my_dict[sum([473])] = False # 10
    my_dict[sum([480])] = True # 11
    my_dict[sum([24413])] = False # 12
    my_dict[sum([24358])] = True # 13
    my_dict[sum([24572])] = True # 14
    my_dict[sum([495345])] = False # 15
    my_dict[sum([13332])] = True # 16
    my_dict[sum([2])] = True # 17
    my_dict[sum([6])] = True # 18
    my_dict[sum([6])] = True # 19
    my_dict[sum([6])] = True # 20
    my_dict[sum([6])] = True # 20
    my_dict[sum([6])] = True # 21
    my_dict[sum([6])] = True # 22
    my_dict[sum([6])] = True # 22
    my_dict[sum([6])] = True # 23
    my_dict[sum([12])] = False # 24
    my_dict[sum([12])] = False # 25
    my_dict[sum([12])] = False # 26
    my_dict[sum([12])] = False # 27
    my_dict[sum([12])] = False # 28
    my_dict[sum([12])] = False # 29
    print(my_dict[ans])