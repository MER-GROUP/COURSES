'''
Итератор Xrange 🌶️
Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает 
три аргумента в следующем порядке:

start — целое или вещественное число
end — целое или вещественное число
step — целое или вещественное число, по умолчанию имеет значение 1

Итератор класса Xrange должен генерировать последовательность членов арифметической 
прогрессии от start до end, включая start и не включая end, с шагом step, а затем 
возбуждать исключение StopIteration.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый 
класс Xrange.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2771335.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.17

Sample Input 1:
evens = Xrange(0, 10, 2)
print(*evens)
Sample Output 1:
0 2 4 6 8

Sample Input 2:
xrange = Xrange(0, 3, 0.5)
print(*xrange, sep='; ')
Sample Output 2:
0.0; 0.5; 1.0; 1.5; 2.0; 2.5

Sample Input 3:
xrange = Xrange(10, 1, -1)
print(*xrange)
Sample Output 3:
10 9 8 7 6 5 4 3 2

Sample Input 4:
xrange = Xrange(5, 10)
print(*xrange)
Sample Output 4:
5 6 7 8 9
'''
pass

if __name__ == '__main__':
    pass