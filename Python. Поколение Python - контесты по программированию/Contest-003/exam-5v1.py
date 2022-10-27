'''
Возрастающая подпоследовательность
Дана последовательность натуральных чисел. Напишите программу, 
которая из данной последовательности вычеркивает минимальное 
количество чисел так, чтобы оставшиеся шли в порядке возрастания.

Формат входных данных
На вход программе подается последовательность натуральных чисел, 
разделенных пробелом. Количество чисел в последовательности не превышает 10000.

Формат выходных данных
Программа должна из введенной последовательности вычеркнуть 
минимальное количество чисел так, чтобы оставшиеся шли в 
порядке возрастания. Не вычеркнутые числа следует вывести 
через пробел, сохранив их исходный порядок следования.  

Примечание 1. Если вариантов вычеркнуть числа несколько, можно вывести любой.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/718107/tests_3019847.zip

tests

Sample Input 1:
2 5 3 4 6 1
Sample Output 1:
2 3 4 6

Sample Input 2:
1 3 5 2 4
Sample Output 2:
1 2 4

Sample Input 3:
5
Sample Output 3:
5
'''
# Решение
class Seq:
    def __init__(self, *args: list) -> None:
        self.algo(args)

    def algo(self, arr: list) -> None:
        '''
        Sample Input 1:
        2 5 3 4 6 1
        Sample Output 1:
        2 3 4 6

        Sample Input 2:
        1 3 5 2 4
        Sample Output 2:
        1 2 4
        '''
        print('----------')###
        print(*arr) # test
        print('----------')###
        res_dict = dict()
        res_arr = list()
        len_arr = len(arr)

        array = list(arr)
        i = 0
        while 0 < len(array): ###
            array_copy = array.copy()
            while 1 < len(array_copy):
                temp_arr = [array_copy[i]]
                if not (i + 1 == len(array_copy)):
                    for j in range(i + 1, len(array_copy)):
                        if (array_copy[j] > temp_arr[-1]):
                            temp_arr.append(array_copy[j])
                res_arr.append(temp_arr)
                res_dict[len(temp_arr)] = temp_arr
                if not (i + 1 == len(array_copy)):
                    del array_copy[i + 1]
            del array[0] ###

        # step = 0
        # for i in arr:
        #     check = True
        #     temp_arr = [i]
        #     if not (step + 1 == len_arr):
        #         for j in arr[step + 1 :]:
        #             if check:
        #                 if (j > temp_arr[-1]):
        #                     temp_arr.append(j)
        #                     check = False
        #             else:
        #                 if (j <= temp_arr[-1]) and (j > temp_arr[-2]):
        #                     temp_arr[-1] = j
        #                 elif (j > temp_arr[-1]):
        #                     temp_arr.append(j)
        #     res_arr.append(temp_arr)
        #     res_dict[len(temp_arr)] = temp_arr
        #     step += 1

        print('----------')###
        print(*res_arr, sep='\n') # test
        print('----------')###
        print(*res_dict.items(), sep='\n') # test
        print('----------')###

if __name__ == '__main__':
    Seq(*map(int, input().split()))