'''
"Обработка данных и функции astype и метод resize"

Исследовательская группа занимается анализом данных из нескольких источников, 
включая базы данных и документы формата CSV. Они часто сталкиваются с проблемой разных 
типов данных и нуждаются в едином формате для обработки данных. Помогите группе изменить 
тип данных в их массивах, используя функцию astype, и повторить данные, используя метод resize, 
чтобы данные имели единый формат для дальнейшей обработки.

В первой строке поступает целое число n - количество массивов с числами, разделенными пробелами. 
Во второй строке - название типа к которому нужно привести элементы всех массивов, 
далее в следующих n строках идут сами массивы.  В последней строке идет целое 
число m - количество элементов, которое должно быть в каждом из массивов. 
Привести тип элементов всех массивов к необходимому типу, также привести 
размерность каждого массива к типу n, если при этом размерность нового массива больше, 
чем исходного, лишние значения заполнить нулями. Вывести все получившиеся массивы 
на экран через пробел.

Sample Input:
2
int
1 10 2 10
1 10 2 10
6
Sample Output:
[ 1 10  2 10  0  0] [ 1 10  2 10  0  0]
'''
import numpy as np

if __name__ == '__main__':
    pass