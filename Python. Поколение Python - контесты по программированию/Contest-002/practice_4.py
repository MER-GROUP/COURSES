'''
Самое скучное условие
Зачастую из-за непонятных условий сложно понять суть задачи, 
поэтому иногда лучше написать коротко и по делу.

Напишите программу, которая находит длину самого длинного палиндрома, 
который можно составить из букв в строке.

Формат входных данных
На вход программе подается одна строка, 
состоящая из строчных латинских букв.

Формат выходных данных
Программа должна вывести одно число — длину самого длинного палиндрома, 
который можно составить из букв в введенной строке.

Примечание 1. Палиндром читается одинаково в обоих направлениях, 
например, слово «rotavator».

Примечание 2. Рассмотрим первый тест. Из букв a, b, a, b, q, t, и d можно 
составить палиндром, например, abqba, длина которого равна 55. 
Палиндром большей длины из данных букв составить нельзя.

Sample Input 1:

ababqtd
Sample Output 1:

5
Sample Input 2:

bebebe
Sample Output 2:

5
Sample Input 3:

qaaaaaaaab
Sample Output 3:

9
'''

'''
Главная идея: самый большой палиндром можно составить, 
если каждую букву брать четное количество. 
Тогда справа и слева можно расположить одинаковое количество 
одинаковых букв. Есть еще один нюанс, одну из букв мы можем взять 
нечетное число раз и расположить по центру, как например в строке 
abbba, букв a - четное количество, букв b - нечетное количество. 
'''

class Algo:
    def __init__(self, s) -> None:
        self.__algo(s)

    def __algo(self, s):
        my_dict = dict()
        for i in s:
            my_dict[i] = my_dict.get(i, 0) + 1
        check = True
        res = int()
        for i in my_dict.values():
            if i % 2 and check:
                res += i
                check = False
            elif 0 == i % 2:
                res += i
            else:
                res += (i -1)
        print(res)

if __name__ == '__main__':
    Algo(input())