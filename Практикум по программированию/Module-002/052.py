'''
Римская система счисления
Дано число X. Требуется перевести это число в римскую систему счисления.

Входные данные
Дано число X в десятичной системе счисления (1  ≤  X  ≤  100).

Выходные данные
Выведите X в римской системе счисления.

Sample Input:
4
Sample Output:
IV
'''
def n_to_rome(n):
    rome = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 
        20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 
        70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C'
    }

    a = n // 100 * 100
    b = n % 100 // 10 * 10
    c = n % 10
    res = str()

    if 0 != a: res += rome[a]
    if 0 != b: res += rome[b]
    if 0 != c: res += rome[c]

    return res

if __name__ == '__main__':
    print(n_to_rome(int(input())))