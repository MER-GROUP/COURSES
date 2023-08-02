'''
Функция nonempty_lines()
Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:

file — название текстового файла, например, data.txt
Функция должна возвращать генератор, порождающий последовательность всех непустых строк 
файла file с убранным символом переноса строки \n. Если строка содержит более 25 символов, 
она заменяется многоточием ....

Примечание 1. При открытии файла используйте явное указание кодировки UTF-8.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию nonempty_lines(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_2785662.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.10

Sample Input 1:
lines = nonempty_lines('file1.txt')
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
Sample Output 1:
bee
geek
stepik
aaaaaaaaaaaaaaaaaaaaaaaaa

Sample Input 2:
print(*nonempty_lines('file2.txt'))
Sample Output 2:
short line another short line ... end of file
'''
from _collections_abc import Generator

pass

if __name__ == '__main__':
    pass