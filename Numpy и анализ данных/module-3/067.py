'''
Анализ данных по зарплатам сотрудников

Имеется массив зарплат сотрудников компании, в котором каждому индексу отвечает 
определенный работник, а значением является зарплата, и необходимо изменить зарплату 
определенных сотрудников. На вход, в первой строке, поступает массив со старой зарплатой 
сотрудников, во второй строке - массив индексов сотрудников, зарплату которых нужно 
изменить. В третьей строке поступает массив с новыми значениями зарплат. На выход 
подайте обновленный массив numpy с обновленными данными по зарплате.

Sample Input:
76 55 60 81 87 84 71 52 79 86 84 83 76
0 2 7
88 65 78
Sample Output:
[88 55 65 81 87 84 71 78 79 86 84 83 76]
'''
import numpy as np

if __name__ == '__main__':
    arr = np.fromstring(string=input(), dtype=int, sep=' ')
    arr_index = np.fromstring(string=input(), dtype=int, sep=' ')
    arr_pay = np.fromstring(string=input(), dtype=int, sep=' ')

    # arr_pay = iter(np.fromstring(string=input(), dtype=int, sep=' '))
    # for i in arr_index:
    #     arr[i] = next(arr_pay)

    arr[arr_index] = arr_pay

    print(arr)