'''
Исполнитель Водолей
У исполнителя “Водолей” есть два сосуда, первый объемом A литров, 
второй объемом B литров, а также кран с водой. 
Водолей может выполнять следующие операции:

1. Наполнить сосуд A (обозначается >A).
2. Наполнить сосуд B (обозначается >B).
3. Вылить воду из сосуда A (обозначается A>).
4. Вылить воду из сосуда B (обозначается B>).
5. Перелить воду из сосуда A в сосуд B (обозначается как A>B).
6. Перелить воду из сосуда B в сосуд A (обозначается как B>A).
7. Команда переливания из одного сосуда в другой приводят к тому, 
что либо первый сосуд полностью опустошается, либо второй сосуд полностью наполняется.

Входные данные

Программа получает на вход три натуральных числа A, B, N, 
не превосходящих 10^4.

Выходные данные

Необходимо вывести алгоритм действий Водолея, который позволяет получить 
в точности N литров в одном из сосудов, если же такого алгоритма не существует, 
то программа должна вывести текст Impossible.

Количество операций в алгоритме не должно превышать 10^5. Гарантируется, 
что если задача имеет решение, то есть решение, которое содержит не более, 
чем 10^5 операций.

Sample Input:
3
5
1
Sample Output:
>A
A>B
>A
A>B
'''
a, b, n = (int(input()) for _ in range(3))
sosud_a, sosud_b = 0, 0

arr = list()
answer = False

if a > b:
    # a > b
    while True:
        print('>A')
        arr.append('>A')
        sosud_a = a
        if n == sosud_a:
            answer = True
            break

        print('A>B')
        arr.append('A>B')
        sosud_a = 0
        sosud_b = b
        if n == sosud_b:
            answer = True
            break

        break

print(f'answer = {answer}')
# a < b
if not answer:
    arr.clear()
    sosud_a, sosud_b = 0, 0
    while True:
        print('>B')
        arr.append('>B')
        sosud_b = b
        print(f'sosud_b = {sosud_b}') ###
        if n == sosud_b:
            print('00000000000000000000000')
            answer = True
            break

        print('B>A')
        arr.append('B>A')
        sosud_b = 0 if sosud_a + b <= a else a - b
        print(f'sosud_b = {sosud_b}') ###
        if n == sosud_b:
            print('11111111111111111111111')
            answer = True
            break
        sosud_a = sosud_a + b if sosud_a + b <= a else a
        print(f'sosud_a = {sosud_a}') ###
        if n == sosud_a:
            print('22222222222222222222222')
            answer = True
            break
        if sosud_a == a:
            break


print(f'answer = {answer}')
if answer:
    print(*arr, sep='\n')
else:
    print('Impossible')