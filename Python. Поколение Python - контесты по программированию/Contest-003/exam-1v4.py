'''
Одиндватри
Рассмотрим последовательность натуральных чисел:
1,2,3,4,5,6,7,8,9,10,11,12,13,14,…
Перевернем в ней каждое число. Получим последовательность:
1,2,3,4,5,6,7,8,9,01,11,21,31,41,…
Запишем полученную последовательность слитно в виде одной строки:
1234567890111213141...

Напишите программу, которая выводит n-ую цифру полученной строки.

Формат входных данных
На вход программе подается натуральное число nn, где 1⩽n⩽10^50

Формат выходных данных
Программа должна вывести nn-ую цифру строки, представленной в условии задачи.

Примечание. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/718107/tests_3019840.zip

Sample Input 1:
10
Sample Output 1:
0

Sample Input 2:
1
Sample Output 2:
1

Sample Input 3:
100
Sample Output 3:
5
'''   
class OdinDvaTri:
    def __init__(self, n: int) -> None:
        self.n = n

    def algo(self) -> str:
        res = str()
        count = int()
        check = False
        for i in range(1, self.n + 1):
            s = str(i)
            if(1 < len(s)):
                rev = s[::-1]
                for c in rev:
                    count += 1
                    if(self.n == count):
                        res = c
                        check = True
                        break
            else:
                count += 1
                if(self.n == count):
                        res = s
                        check = True
                        break
            if check:
                break
        return res

if __name__ == '__main__':
    print(OdinDvaTri(int(input())).algo())
