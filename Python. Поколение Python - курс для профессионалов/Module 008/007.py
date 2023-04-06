'''
Песочные часы
Напишите программу с использованием рекурсивной функции, 
которая выводит изображение песочных часов, составленное из цифр 1, 2, 3, и 4:

1111111111111111    # 16 раз
  222222222222      # 12 раз
    33333333        # 8 раз
      4444          # 4 раза
    33333333        # 8 раз
  222222222222      # 12 раз
1111111111111111    # 16 раз

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести изображение песочных часов, составленное 
из цифр 1, 2, 3, и 4, представленное в условии задачи.

Примечание. Количество цифр в каждой строке, указанное в комментариях, 
выводить не нужно.
'''
def clock():
    _n = 16
    _space = 0
    _num = 1
    def rec(n=_n, space=_space, num=_num):
        if 4 < n:
            print(' ' * space + f'{num}' * n + ' ' * space)
            rec(n-4, space+2, num+1)
        print(' ' * space + f'{num}' * n + ' ' * space)
    rec(_n, _space, _num)

if __name__ == '__main__':
    clock()