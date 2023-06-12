'''
Delete

На вход поступают две строки. В первой строке содержится последовательность 
целых чисел, разделенных пробелом, во второй строке целое число i. Из первой 
строки нужно создать массив numpy и затем удалить из него с помощью 
функции delete() элемент с индексом i. Выведите на экран исходный 
и итоговый массивы, каждый с новой строки.

Sample Input:
28 22 24 9 32 33 53 27 50 30 48 49
4
Sample Output:
[28 22 24  9 32 33 53 27 50 30 48 49]
[28 22 24  9 33 53 27 50 30 48 49]
'''
import numpy as np

if __name__ == '__main__':
    arr = np.array(input().split(), dtype=int)
    print(arr)
    arr = np.delete(arr=arr, obj=int(input()))
    print(arr)