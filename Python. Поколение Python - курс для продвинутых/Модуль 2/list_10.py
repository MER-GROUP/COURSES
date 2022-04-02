# обработка вложенного списка
print('##########')
list1 = [[1, 2, 3], [4, 5]]
list2 = list1

list1[0].append(7)

print(list2)

# обработка вложенного списка
print('##########')
list1 = [[1] * 3] * 3
list1[0][1] = 5

print(list1)

# обработка вложенного списка
print('##########')
n = 3
list1 = []

for _ in range(n):
    row = input().split()
    list1.extend(row)

print(list1)

# обработка вложенного списка
print('##########')
my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = max(row)
    minimum = min(row)

print(maximum + minimum)

# обработка вложенного списка
print('##########')
my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)

print(maximum + minimum)