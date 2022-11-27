'''
Знак числа
В математике функция sign(x) (знак числа) определена так: 
sign(x) = 1,   если x > 0, 
sign(x) = -1, если x < 0, 
sign(x) = 0,   если x = 0.

Для данного числа x выведите значение sign(x).

Входные данные
Вводится число x.

Выходные данные
Выведите ответ на задачу.

Sample Input:
115
Sample Output:
1
'''
def sign(x):
    if 0 < x:
        return 1
    elif 0 > x:
        return -1
    else:
        return 0

print(
    # (lambda x: sign(x))(int(input()))
    *map(sign, [int(input())])
)