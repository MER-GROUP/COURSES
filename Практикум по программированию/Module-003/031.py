'''
Удаление фрагмента
Дана строка, в которой буква h встречается минимум два раза 
это может быть как маленькая буква h, так и заглавная H). 
Удалите из этой строки первое и последнее вхождение буквы h, 
а также все символы, находящиеся между ними.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input:
In the hole in the ground there lived a hobbit
Sample Output:
In tobbit
'''
import sys  

sys.stdin = open(file='031.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
print(arr) # test

pass