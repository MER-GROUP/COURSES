'''
Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1 разделённую на общее количество всех чисел.
Подсказка
Используйте встроенные функции sum() и len() для нахождения суммы всех элементов и их количества. 
'''

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
list_simple = [el for li in list1 for el in li ]
	
print(sum(list_simple) / len(list_simple))