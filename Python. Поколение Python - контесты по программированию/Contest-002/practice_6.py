'''
Повторяйповторяйповторяй
Напишите программу, которая определяет, на какое максимальное количество 
одинаковых подстрок можно разбить данную строку так, чтобы 
все элементы строки были задействованы.

Формат входных данных
На вход программе подается одна строка, состоящая из строчных латинских букв., 
длина которой не превышает 400000 символов.

Формат выходных данных
Программа должна вывести одно натуральное число — максимальное количество 
подстрок в разбиении из условия.

Примечание 1. Рассмотрим первый тест. Строку abcabcabc можно разбить 
на 3 одинаковые подстроки: abc, abc и abc.

Примечание 2. Рассмотрим шестой тест. Строку bebebeb можно разбить 
на единственную подстроку bebebeb, соответствующую исходной. 
Разбиение на подстроки, например, be или beb невозможно, 
так как в любом случае остаются незадействованные элементы строки.

Sample Input 1:

abcabcabc
Sample Output 1:

3
Sample Input 2:

acdc
Sample Output 2:

1
Sample Input 3:

bbbbbb
Sample Output 3:

6
Sample Input 4:

abobaboabobabo
Sample Output 4:

2
Sample Input 5:

abobaboaaabobaboaa
Sample Output 5:

2
Sample Input 6:

bebebeb
Sample Output 6:

1
'''

class Algo:
    def __init__(self, s) -> None:
        self.__algo(s)

    # максимальное количество подстрок
    def __algo(self, s):
        length = len(s)
        word = str()
        half = int(length / 2)
        res = int(1)
        for i in range(0, half + 1):
            word += s[i]
            cnt = s.count(word)
            if (len(word) * cnt) == length:
                res = cnt
                break
        print(res)

    # минимальное количество подстрок
    def __algo2(self, s):
        length = len(s)
        word = str()
        half = int(length / 2)
        res = int(1)
        for i in range(half, -1 , -1):
            word = s[: i + 1]
            cnt = s.count(word)
            if (len(word) * cnt) == length:
                res = cnt
                break
        print(res)

if __name__ == '__main__':
    Algo(input())