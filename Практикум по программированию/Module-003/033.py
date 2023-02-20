'''
Дублирование фрагмента
Дана строка, в которой буква h встречается как минимум два раза. 
Повторите последовательность символов, заключенную между первым 
и последним появлением буквы h два раза, сами буквы h повторять не надо.

Имейте ввиду, в тексте могут встречаться заглавные буквы H.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input:
In the hole in the ground there lived a hobbit
Sample Output:
In the hole in the ground there lived a e hole in the ground there lived a hobbit
'''
import sys  

sys.stdin = open(file='033.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
print(arr) # test

pass