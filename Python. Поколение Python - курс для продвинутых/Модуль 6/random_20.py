# Болотная сортировка
# (Bogosort)
from random import shuffle

# отсортирован ли список?
def is_sort(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

# реализация алгоритма болотной сортировки
def bogosort(nums):
    while not is_sort(nums):
        shuffle(nums)
    return nums

numbers = list(range(10))
# перемешиваем начальный список
shuffle(numbers)
# выводим начальный список
print(numbers)

sorted_numbers = bogosort(numbers)

# выводим отсортированный список
print(sorted_numbers)