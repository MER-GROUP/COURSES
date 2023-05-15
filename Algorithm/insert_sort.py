# def insertion_sort(nums):
#     # Сортировку начинаем со второго элемента, 
#     # т.к. считается, что первый элемент уже отсортирован
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         # Сохраняем ссылку на индекс предыдущего элемента
#         j = i - 1
#         # Элементы отсортированного сегмента перемещаем вперёд, 
#         # если они больше элемента для вставки
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j -= 1
#         # Вставляем элемент
#         nums[j + 1] = item_to_insert

def insertion_sort(arr: list) -> None:
    for i in range(1, len(arr)):
        element_to_insert = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > element_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element_to_insert

# Проверяем, что оно работает
if __name__ == '__main__':
    from random import randint

    N = 10
    arr = [randint(1, 99) for item in range(N)]
    
    print(arr)
    insertion_sort(arr)
    print(arr)