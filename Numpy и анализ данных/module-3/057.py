'''
Задача о Золотой Рыбке

Волшебная рыбка просит вас помочь ей отсортировать массив чисел. Она хочет, 
чтобы вы взяли первые 5 элементов массива и отсортировали их по убыванию. 
Затем вы должны взять последние 3 элемента массива и отсортировать их по возрастанию. 
Затем выведите получившийся массив в виде чисел, разделенных пробелом, на экран. 
Если вы выполните ее просьбу, она исполнит любое ваше желание.

Sample Input:
37 41 37 37 41 38 33 37 38 41 3
Sample Output:
41 41 37 37 37 3 38 41
'''
import numpy as np

if __name__ == '__main__':
    arr = np.fromstring(string=input(), dtype=int, sep=' ')
    print(*np.sort(a=arr[:5])[::-1], *np.sort(a=arr[-3:]))