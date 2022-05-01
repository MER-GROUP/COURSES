# авторский алгоритм от BEEGIK
# Решение. Подход к решению этой задачи, который будет описан ниже, 
# основан на двумерном динамическом программировании.

# Главная идея решения: двумерный список array хранит входные данные. 
# Строим двумерный динамический список new_array с таким свойством: 
# new_array[i][j] - это минимальное время, за которое робот смог добраться 
# до ячейки с индексами [i][j]. Теперь пусть в new_array[i-1][j] минимальное время, 
# за которое робот смог добраться до ячейки с индексами [i-1][j], 
# а в new_array[i][j-1] тоже минимальное время только до точки [i][j-1]. 
# Тогда существует такой инвариант алгоритма: new_array[i][j] = min(new_array[i-1][j], 
# new_array[i][j-1]) + array[i][j], в случае если в ячейки [i-1][j] и [i][j-1] 
# можно добраться.  Осталось аккуратно обработать нулевую строку и нулевой столбец, 
# а также случаи, когда в какую-нибудь из клеток [i-1][j] или [i][j-1] нельзя добраться.

# Как строим путь: в каждую точку, которую мы попали, мы записываем 11, 
# если в нее пришли слева, и 00, если пришли справа. Что значит, 
# пришли слева или сверху? Например, если мы пришли слева - это значит, 
# что в левую ячейку мы добрались быстрее, чем в верхнюю, и аналогично, 
# если пришли сверху. Таким образом, если путь существует, то его мы 
# восстанавливаем с финишной ячейки. Там ставим 

#. Если в финишной стоит 11, то сдвигаемся в ячейку слева и там ставим #, 
# если в финишной 00, то сдвигаемся вверх и там ставим #. 
# Для новой ячейки повторяем это условие. Опять же если путь существует, 
# то мы попадем в стартовую ячейку.

n = int(input())
# список исходных значений
array = [] 
# динамический список
new_array = [] 
# список для восстановления ходов (0 - пришел в текущую ячейку сверху, 1 - соответственно слева)
tuple_array = [] 
# результирующая табла с # и -
result = [] 

# заполняем все списки
for i in range(n):
    string = input()
    array.append([int(i) for i in string])
    tuple_array.append([-1 for _ in range(n)])
    new_array.append([0 for _ in range(n)])
    result.append(['-' for _ in range(n)])


new_array[0][0] = array[0][0]

# обработка первой строки
for columns in range(1, n):
    if array[0][columns] == 0:
        new_array[0][columns] = 0
    else:
        if new_array[0][columns - 1] == 0:
            new_array[0][columns] = 0
        else:
            new_array[0][columns] = new_array[0][columns - 1] + array[0][columns]
            tuple_array[0][columns] = 1

# обработка первого столбца
for rows in range(1, n):
    if array[rows][0] == 0:
        new_array[rows][0] = 0
    else:
        if new_array[rows - 1][0] == 0:
            new_array[rows][0] = 0
        else:
            new_array[rows][0] = new_array[rows - 1][0] + array[rows][0]
            tuple_array[rows][0] = 0

# обработка остальных ячеек
for i in range(1, n):
    for j in range(1, n):
        if array[i][j] == 0:
            continue
        if new_array[i - 1][j] == 0 and new_array[i][j - 1] == 0:
            new_array[i][j] = 0
        elif new_array[i - 1][j] == 0:
            new_array[i][j] = new_array[i][j - 1] + array[i][j]
            tuple_array[i][j] = 1
        elif new_array[i][j - 1] == 0:
            new_array[i][j] = new_array[i - 1][j] + array[i][j]
            tuple_array[i][j] = 0
        else:
            if new_array[i - 1][j] >= new_array[i][j - 1]:
                new_array[i][j] = new_array[i][j - 1] + array[i][j]
                tuple_array[i][j] = 1
            else:
                new_array[i][j] = new_array[i - 1][j] + array[i][j]
                tuple_array[i][j] = 0

if new_array[-1][-1] == 0:
    print('Impossible')
else:
    result[0][0] = '#'
    i, j = n - 1, n - 1
    while (i != 0 or j != 0):
        if tuple_array[i][j] == 1:
            result[i][j] = '#'
            j -= 1
        else:
            result[i][j] = '#'
            i -= 1
    for i in result:
        print(*i, sep='')