# heapify - создать кучу
def heapify(arr: list, i: int, heap='max') -> None:
    """
    функция heapify - создать кучу\n
    \t arr - массив\n
    \t i - первый нелистовой узел, его индекс равен n/2 - 1\n
    \t heap='max|min' - максимальный или минимальный начальный элемент кучи\n
    i - индекс текущего узла\n
    arr[i] - текущий элемент массива - current_element\n
    n - размер массива (кучи)
    """
    # размер кучи
    n = len(arr) - 1
    # индекс наибольшего узла
    largest = i 
    # индекс левого дочернего элемента
    left_child = 2*i + 1 
    # индекс правого дочернего элемента
    right_child = 2*i + 2 
    # left_child меьше или равно n
    # и left_child больше, чем current_element
    # то largest присваивается left_child
    if left_child <= n and arr[left_child] > arr[largest]:
        largest = left_child
    # right_child меьше или равно n
    # и right_child больше, чем current_element
    # то largest присваивается right_child
    if right_child <= n and arr[right_child] > arr[largest]:
        largest = right_child
    # если индекс наибольшего узла не равен индексу текущего узла
    # обменяем значения largest и current_element
    if not largest == i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # рекурсивно создаем кучу
        heapify(arr, largest)

# heap_max - создать max кучу
def heap_max(arr: list) -> None:
    # размер кучи
    n = len(arr)
    # цикл от первого индекса нелистового узла до 0
    for i in range(n//2 - 1, -1, -1):
        # создаем кучу
        heapify(arr, i)





# # heap_min - создать min кучу
# def heap_min(arr: list) -> None:
#     # размер кучи
#     n = len(arr)
#     # цикл от первого индекса нелистового узла до 0
#     for i in range(n//2 - 1, -1, -1):
#         # создаем кучу
#         heapify(arr, i)

if __name__ == '__main__':
    from random import randint

    N = 6
    # a = []
    # for i in range(N):
    #     a.append(randint(1, 99))
    a = [3, 9, 2, 1, 4, 5]
    b = [3, 9, 2, 1, 4, 5]
    c = [3, 9, 2, 1, 4, 5]
    
    print(a)
    # heapify(a, (len(a)//2) - 1)
    heapify(a, 0)
    print(a)
    heap_max(b)
    print(b)