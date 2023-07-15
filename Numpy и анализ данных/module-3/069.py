'''
Безопасная архивация

Компания хочет сделать резервную копию важных данных на дополнительном жестком диске, 
но не хочет рисковать потерей данных, если что-то пойдет не так. Чтобы обезопасить себя, 
компания создаст копию одномерного numpy массива, содержащего информацию о данных, и заменит 
в копии все значения, которые являются конфиденциальной информацией, на случайные значения. 
Таким образом, можно создать безопасную архивную копию, не рискуя утечкой данных.

На вход подается массив целых чисел, разделенных пробелом - а. Во второй строке подается 
массив индексов значений в массиве а которые нужно изменить. В третьей строке подаются новые 
значения, соответствующие этим индексам. На выход необходимо подать старый numpy массив а 
с первоначальными значениями и новую его копию с измененными данными.

Sample Input:
82 80 70 95 82 87 66 68 91 59 53 79 58 91
0 1 4 5
8 8 8 8
Sample Output:
[82 80 70 95 82 87 66 68 91 59 53 79 58 91]
[ 8  8 70 95  8  8 66 68 91 59 53 79 58 91]
'''
import numpy as np

if __name__ == '__main__':
    pass