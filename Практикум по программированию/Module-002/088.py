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
###################################
def a_ge_b(a, b, n):
    print('---a_ge_b---') # test
    arr = list()
    sosud_a, sosud_b = 0, 0
    check = False

    if a >= b:
        while True:
            print('>A') # test
            arr.append('>A')
            sosud_a = a
            if n == sosud_a:
                check = True
                break

            print('A>B') # test
            arr.append('A>B')
            sosud_a = 0
            sosud_b = b
            if n == sosud_b:
                check = True
                break

            break
    
    print('-----end----') # test
    return check, arr
###################################
def b_ge_a(a, b, n):
    print('---b_ge_a---') # test
    arr = list()
    sosud_a, sosud_b = 0, 0
    check = False

    if b >= a:
        while True:
            print('>B') # test
            arr.append('>B')
            sosud_b = b
            if n == sosud_b:
                check = True
                break

            print('B>A') # test
            arr.append('B>A')
            sosud_b = 0
            sosud_a = a
            if n == sosud_a:
                check = True
                break

            break
    
    print('-----end----') # test
    return check, arr
###################################
def a_le_b(a, b, n):
    print('---a_le_b---') # test
    arr = list()
    sosud_a, sosud_b = 0, 0
    check = False

    if a <= b:
        while True:
            print('>A')
            arr.append('>A')
            sosud_a = a
            if n == sosud_a:
                check = True
                break

            print('A>B')
            arr.append('A>B')
            sosud_a = 0 if sosud_b + a <= b else sosud_b + a - b
            if n == sosud_a:
                check = True
                break
            sosud_b = sosud_b + a if sosud_b + a <= b else b
            if n == sosud_b:
                check = True
                break
            if sosud_b == b: # exit func
                break

    print('-----end----') # test
    return check, arr
###################################
def b_le_a(a, b, n):
    pass
###################################
def a_le_2_b(a, b, n):
    pass
###################################
def b_le_2_a(a, b, n):
    pass
###################################
if __name__ == '__main__':
    a, b, n = (int(input()) for _ in range(3))
    flag = False
    check = False
    
    if not check and not flag: 
        check, arr = a_ge_b(a, b, n)
        print('a_ge_b')
        if check: print(*arr, sep='\n')
        if check: flag = True

    if not check and not flag:
        check, arr = b_ge_a(a, b, n)
        print('b_ge_a')
        if check: print(*arr, sep='\n')
        if check: flag = True 

    if not check and not flag:
        check, arr = a_le_b(a, b, n)
        print('a_le_b')
        if check: print(*arr, sep='\n')
        if check: flag = True 

    if not check and not flag:
        print('b_le_a')

    if not check and not flag:
        print('a_le_2_b')

    if not check and not flag:
        print('b_le_2_a')

    if not check and not flag:
        print('Impossible')
###################################