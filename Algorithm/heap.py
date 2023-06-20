# heapify - создать кучу
def heapify(arr: list, i: int) -> None:
    """
    функция heapify - создать кучу\n
    \t arr - массив\n
    \t i - первый нелистовой узел, его индекс равен n/2 - 1\n
    i - индекс текущего узла\n
    arr[i] - текущий элемент массива - current_element\n
    """
    # размер кучи
    n = len(arr) - 1
    # индекс наибольшего узла
    largest = i 
    # индекс левого дочернего элемента
    # left_child = 2*i + 1 
    left_child = 2*i #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # индекс правого дочернего элемента
    # right_child = 2*i + 2 
    right_child = 2*i + 1 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
        # heapify(arr, largest)

if __name__ == '__main__':
    from random import randint

    N = 6
    # a = []
    # for i in range(N):
    #     a.append(randint(1, 99))
    a = [3, 9, 2, 1, 4, 5]
    
    print(a)
    heapify(a, (len(a)//2) - 1)
    # heapify(a, 1)
    print(a)