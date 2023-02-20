'''
Обращение фрагмента
Дана строка, в которой буква h встречается как минимум два раза. 
Разверните последовательность символов, заключенную между 
первым и последним появлением буквы h, в противоположном порядке.

Имейте ввиду, в тексте могут встречаться заглавные буквы H.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input:
In the hole in the ground there lived a hobbit
Sample Output:
In th a devil ereht dnuorg eht ni eloh ehobbit
'''
import sys  

# sys.stdin = open(file='032.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

start = arr.lower().find('h')
end = arr.lower().rfind('h')

print(arr.replace(arr[start + 1 : end], arr[start + 1 : end][::-1]))