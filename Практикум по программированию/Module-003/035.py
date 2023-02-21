'''
Удаление символа
Дана строка. Удалите из этой строки все символы @.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input:
Bilbo.Baggins@bagend.hobbiton.shire.me
Sample Output:
Bilbo.Bagginsbagend.hobbiton.shire.me
'''
import sys  

# sys.stdin = open(file='035.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

print(arr.replace('@', ''))