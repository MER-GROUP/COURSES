'''
"Хроники Средиземья"

Главный историк Средиземья ведет записи о событиях, происходящих в мире. 
Он создает массив numpy из объектов datetime, представляющих даты ключевых 
событий в истории мира. Выведите на экран тип данных массива, даты самого 
раннего и самого позднего событий.

Sample Input:
1598-04-29 1711-11-28 1661-05-06 0869-11-22 0930-05-22 0987-05-06 0827-05-22 1029-11-04 1255-02-12 1123-11-13 1697-03-17 1384-01-21 1408-06-10 1166-09-04 1109-09-18
Sample Output:
object 0827-05-22 1711-11-28
'''
import numpy as np
from datetime import datetime

if __name__ == '__main__':
    arr = np.array(
        object=[datetime.strptime(s, '%Y-%m-%d').date() for s in input().split()],
        dtype=np.object_
    )
    print(
        arr.dtype,
        arr.min(),
        arr.max()
    )

    # a = np.array(input().split(), dtype = object)
    # print(a.dtype,  a.min(), a.max())