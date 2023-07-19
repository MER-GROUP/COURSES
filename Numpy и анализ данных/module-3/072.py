'''
Зачарованный сад

В далеком царстве есть сад, в котором растут фрукты разных видов. Каждый фрукт имеет свой цвет, 
который соответствует определенному числу. Сад зачарован, и фрукты каждый день увеличивают 
свою массу на 20%, а цвет становится ярче на 15%. Царь хочет знать, через сколько дней цвет 
каждого фрукта превысит определенную отметку, равную 100. Помогите царю узнать это и 
выведите на экран целое число - количество дней, спустя которое цвет каждого фрукта станет 
не менее 100, в следующей строке выведите итоговый массив со значениями цветов каждого фрукта 
спустя данный промежуток времени.

На вход поступает строка действительных чисел, разделенных пробелом, значение каждого 
числа - цвет соответствующего фрукта в условных единицах. 

Sample Input:
2 10 16 14 20 24 28 8 29 9 13 23 29 6 28 10
Sample Output:
28
[ 100.13122413  500.65612066  801.04979305  700.91856892 1001.31224131
 1201.57468957 1401.83713784  400.52489652 1451.9027499   450.59050859
  650.85295685 1151.50907751 1451.9027499   300.39367239 1401.83713784
  500.65612066]
'''
import numpy as np

if __name__ == '__main__':
    arr = np.fromstring(string=input(), dtype=None, sep=' ')
    # while 100 > np.amin():
    #     ...