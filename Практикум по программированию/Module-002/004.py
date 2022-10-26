'''
Дележ яблок - 2
N школьников делят K яблок поровну, 
неделящийся остаток остается в корзинке. 
Сколько яблок останется в корзинке?

Входные данные
Программа получает на вход числа N и K.

Выходные данные
Программа должна вывести искомое количество яблок.

Tests:

Sample Input:
5
21
Sample Output:
1
'''
# (lambda x: print(x[1] % x[0]))([int(input()) for _ in range(2)])

def apple_div (school_cnt, apple_cnt):
    if apple_cnt < school_cnt:
        return apple_cnt
    return apple_div (school_cnt, apple_cnt-school_cnt)
    
print(apple_div(int(input()), int(input())))