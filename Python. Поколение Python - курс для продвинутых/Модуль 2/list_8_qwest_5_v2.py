'''
Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1 разделённую на общее количество всех чисел.
Подсказка
Используйте встроенные функции sum() и len() для нахождения суммы всех элементов и их количества. 
'''

# переводим даумерный массив в одномерный масчив добавлением пустого списка []
list1 = sum([[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]], [])

print(list1)
	
print(sum(list1) / len(list1))