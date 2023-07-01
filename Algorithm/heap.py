# heapify - создать кучу
def heapify(arr: list, i: int, *, heap='max') -> None:
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
    # индекс наибольшего/наименьшего узла
    largest_smallest = i 
    # индекс левого дочернего элемента
    left_child = 2*i + 1 
    # индекс правого дочернего элемента
    right_child = 2*i + 2 
    
    # определяем вид кучи - по убыванию или возростанию
    if 'max' == heap:
        # left_child меьше или равно n
        # и left_child больше, чем current_element
        # то largest_smallest присваивается left_child
        # largest_smallest - сдесь это наибольший индекс
        if left_child <= n and arr[left_child] > arr[largest_smallest]:
            largest_smallest = left_child
        # right_child меьше или равно n
        # и right_child больше, чем current_element
        # то largest_smallest присваивается right_child
        # largest_smallest - сдесь это наибольший индекс
        if right_child <= n and arr[right_child] > arr[largest_smallest]:
            largest_smallest = right_child
    else:
        # left_child меьше или равно n
        # и left_child меьше, чем current_element
        # то largest_smallest присваивается left_child
        # largest_smallest - сдесь это наименьший индекс
        if left_child <= n and arr[left_child] < arr[largest_smallest]:
            largest_smallest = left_child
        # right_child меьше или равно n
        # и right_child меьше, чем current_element
        # то largest_smallest присваивается right_child
        # largest_smallest - сдесь это наименьший индекс
        if right_child <= n and arr[right_child] < arr[largest_smallest]:
            largest_smallest = right_child
    
    # если индекс наибольшего/наименьшего узла не равен индексу текущего узла
    # обменяем значения largest_smallest и current_element
    if not largest_smallest == i:
        arr[i], arr[largest_smallest] = arr[largest_smallest], arr[i]
        # рекурсивно создаем кучу
        heapify(arr, largest_smallest, heap=heap)

# heap_max - создать max кучу
def heap_max(arr: list) -> None:
    # размер кучи
    n = len(arr)
    # цикл от первого индекса нелистового узла до 0
    for i in range(n//2 - 1, -1, -1):
        # создаем кучу по убыванию
        heapify(arr, i, heap='max')

# heap_min - создать min кучу
def heap_min(arr: list) -> None:
    # размер кучи
    n = len(arr)
    # цикл от первого индекса нелистового узла до 0
    for i in range(n//2 - 1, -1, -1):
        # создаем кучу по возростанию
        heapify(arr, i, heap='min')

# heap_insert - вставка нового элемента в кучу
def heap_insert (arr: list, value: int, *, heap='max') -> None:
    ...

if __name__ == '__main__':
    from random import randint

    N = 6
    # a = []
    # for i in range(N):
    #     a.append(randint(1, 99))
    a = [3, 9, 2, 1, 4, 5]
    b = [3, 9, 2, 1, 4, 5]
    c = [3, 9, 2, 1, 4, 5]
    d = [3, 9, 2, 1, 4, 5]
    
    print('----------origin:--------')
    print(a)

    print('---------heapify max:----------')
    # heapify(b, (len(a)//2) - 1)
    print(b)
    # heapify(b, 0)
    heapify(b, 0, heap='max')
    print(b)

    print('----------heap_max:----------')
    print(c)
    heap_max(c)
    print(c)

    print('----------heap_min:----------')
    print(d)
    heap_min(d)
    print(d)