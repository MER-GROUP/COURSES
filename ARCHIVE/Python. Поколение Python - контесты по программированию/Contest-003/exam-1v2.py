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
class ExamTimer:
    def __init__(self, n: int) -> None:
        from threading import Timer
        self.t = Timer(n, self.exit)

    def cancel(self):
        self.t.cancel()

    def exit(self):
        print('Алгоритм не успел решить задачу по времени')
        __import__('os').abort()

    def start(self):
        self.t.start()
    
class OdinDvaTri:
    def __init__(self, n: int) -> None:
        self.my_list = range(1, n + 1)
        self.n = n

    def algo(self) -> str:
        timer = ExamTimer(2)
        timer.start()
        my_list = map(
            lambda x: str(x) if(1 == len(str(x))) else str(x)[::-1],
            self.my_list
        )
        timer.cancel()
        return ''.join(list(my_list))[self.n - 1]

if __name__ == '__main__':
    print(OdinDvaTri(int(input())).algo())