'''
Строка слов
На вход подается строка слов, разделенных пробелом, создайте одномерный 
массив numpy, содержащий эти слова. Выведите массив на экран.

Sample Input:
sd dns sdksl sj
Sample Output:
['sd' 'dns' 'sdksl' 'sj']
'''
import numpy as np

print(np.array(input().split()))