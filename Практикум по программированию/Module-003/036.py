'''
Замена внутри фрагмента
Дана строка. Замените в этой строке все появления буквы h на букву H, 
кроме первого и последнего вхождения.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input:
In the hole in the ground there lived a hobbit
Sample Output:
In the Hole in tHe ground tHere lived a hobbit
'''
import sys  

# sys.stdin = open(file='036.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

start = arr.lower().find('h')
end = arr.lower().rfind('h')
print(arr.replace(arr[start+1 : end], arr[start+1 : end].replace('h', 'H')))