'''
"Операция 'Кармен'"

Детектив Джо Ривера получил информацию о местонахождении опасного преступника 
по кличке Кармен. Он создает массив numpy из булевых значений, где True означает 
наличие признаков, свидетельствующих о присутствии Кармен на заданной территории. 
Определите тип данных массива и выведите на экран количество локаций, в которых 
может находиться Кармен.

Sample Input:
True False  True  True  True  True  True  True False False  True  True True False False False  True  True  True  True  True False  True  True True  True False  True False  True False  True False False  True
Sample Output:
23 bool
'''
import numpy as np

if __name__ == '__main__':
    arr = np.array(
        object=[(False, True)[b == 'True'] for b in input().split()], 
        dtype=np.bool_
    )
    print(arr[arr].size, arr.dtype)