# создание вложенного списка
print('##########')
my_list = [[0], [1, 2], [3, 4, 5]]
print(my_list)

# создание вложенного списка
print('##########')
n, m = 5, 2
my_list = []

for _ in range(n):
    my_list.append([0] * m)

print(my_list)

# создание вложенного списка
print('##########')
n, m = 5, 2
my_list = [0] * n

for i in range(n):
    my_list[i] = [0] * m

print(my_list)

# создание вложенного списка
print('##########')
n, m = 5, 2

my_list = [[0] * m for _ in range(n)]

print(my_list)

# семантическая ошибка
# так делать нельзя
# создание вложенного списка
print('##########')
n, m = 5, 2

my_list = [[0] * m ] * n
my_list[0][0] = 17

print(my_list)

# создание вложенного списка
print('##########')
n = 3
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]
    my_list.append(elem)
print(my_list)

# создание списка
print('##########')
n = 3
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]
    my_list.extend(elem)
print(my_list)

# вывод вложенного списка
print('##########')
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(my_list[0][0])
print(my_list[1][2])
print(my_list[2][1])

# вывод вложенного списка
print('##########')
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')
    print()
    
# вывод вложенного списка
print('##########')
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for elem in row:
        print(elem, end=' ')
    print()
    
# вывод вложенного списка
print('##########')
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')
    print()
    
# обработка вложенного списка
print('##########')
my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        total += my_list[i][j]
print(total)

# обработка вложенного списка
print('##########')
my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for row in my_list:
    for elem in row:
        total += elem
print(total)

# обработка списка
print('##########')
my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for row in my_list:
    total += sum(row)
print(total)