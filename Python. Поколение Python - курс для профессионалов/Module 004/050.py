'''
Одинокая функция
Дан pickle файл, содержащий единственную сериализованную функцию. 
Напишите программу, которая вызывает данную функцию с заданными аргументами и выводит 
возвращаемое значение функции.

Формат входных данных
На вход программе в первой строке подается название pickle файла, 
в котором содержится единственная сериализованная функция. 
Далее подается произвольное количество строк, каждая из которых 
содержит позиционный аргумент для этой функции.

Формат выходных данных
Программа должна вызвать функцию из указанного pickle файла 
со всеми введенными строковыми аргументами, и вывести возвращаемое 
значение функции. Причем аргументы должны быть переданы в том порядке, 
в котором они были введены.

Примечание 1. Аргументы, передаваемые в функцию, должны иметь тип str.

Примечание 2. Рассмотрим первый тест. Сначала подается название файла — func.pkl, 
в котором содержится сериализованная функция:

def func(*args):
    return ' '.join(args)
затем аргументы для этой функции: Hello,, how, are, you и today?.

Программа выводит результат следующего вызова:

func('Hello,', 'how', 'are', 'you', 'today?')

Примечание 3. Для считывания произвольного количества строк используйте 
потоковый ввод sys.stdin.

Примечание 4. Считайте, что вводимый файл находится в папке с программой.

Примечание 5. В этой задаче за кулисами реализовано две функции с именами func и add. 
Не используйте эти имена для именования своих переменных во избежание ошибок.

Sample Input:
func.pkl
Hello,
how
are
you
today?

Sample Output:
Hello, how are you today?
'''
import pickle
import sys

arr = list(map(str.strip, sys.stdin.readlines()))

with open(file=arr[0], mode='rb') as pickle_opener:
    func_from_pickle = pickle.load(file=pickle_opener)

print(func_from_pickle(*arr[1:]))