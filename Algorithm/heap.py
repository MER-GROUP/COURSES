# heapify - создать кучу
def heapify(_arr: list, _i: int, *, _heap='max') -> None:
    """
    функция heapify - создать кучу\n
    \t _arr - массив/куча\n
    \t _i - первый нелистовой узел, его индекс равен _n/2 - 1\n
    \t _heap='max|min' - максимальный или минимальный начальный элемент кучи\n
    _i - индекс текущего узла\n
    _arr[_i] - текущий элемент массива - _current_element\n
    _n - размер массива (кучи)
    """
    # размер кучи
    _n = len(_arr) - 1
    # индекс наибольшего/наименьшего узла
    _largest_smallest = _i 
    # индекс левого дочернего элемента
    _left_child = 2*_i + 1 
    # индекс правого дочернего элемента
    _right_child = 2*_i + 2 
    
    # определяем вид кучи - по убыванию или возростанию
    if 'max' == _heap:
        # _left_child меьше или равно _n
        # и _left_child больше, чем _current_element
        # то _largest_smallest присваивается _left_child
        # _largest_smallest - сдесь это наибольший индекс
        if _left_child <= _n and _arr[_left_child] > _arr[_largest_smallest]:
            _largest_smallest = _left_child
        # _right_child меьше или равно _n
        # и _right_child больше, чем _current_element
        # то _largest_smallest присваивается _right_child
        # _largest_smallest - сдесь это наибольший индекс
        if _right_child <= _n and _arr[_right_child] > _arr[_largest_smallest]:
            _largest_smallest = _right_child
    else:
        # _left_child меьше или равно _n
        # и _left_child меньше, чем _current_element
        # то _largest_smallest присваивается _left_child
        # _largest_smallest - сдесь это наименьший индекс
        if _left_child <= _n and _arr[_left_child] < _arr[_largest_smallest]:
            _largest_smallest = _left_child
        # _right_child меьше или равно _n
        # и _right_child меьше, чем _current_element
        # то _largest_smallest присваивается _right_child
        # _largest_smallest - сдесь это наименьший индекс
        if _right_child <= _n and _arr[_right_child] < _arr[_largest_smallest]:
            _largest_smallest = _right_child
    
    # если индекс наибольшего/наименьшего узла не равен индексу текущего узла
    # обменяем значения _largest_smallest и _current_element
    if not _largest_smallest == _i:
        _arr[_i], _arr[_largest_smallest] = _arr[_largest_smallest], _arr[_i]
        # рекурсивно создаем кучу
        heapify(_arr=_arr, _i=_largest_smallest, _heap=_heap)

# heap_max - создать max кучу
def heap_max(_arr: list) -> None:
    # размер кучи
    _n = len(_arr)
    # цикл от первого индекса нелистового узла до 0
    for _i in range(_n//2 - 1, -1, -1):
        # создаем кучу по убыванию
        heapify(_arr=_arr, _i=_i, _heap='max')

# heap_min - создать min кучу
def heap_min(_arr: list) -> None:
    # размер кучи
    _n = len(_arr)
    # цикл от первого индекса нелистового узла до 0
    for _i in range(_n//2 - 1, -1, -1):
        # создаем кучу по возростанию
        heapify(_arr=_arr, _i=_i, _heap='min')

# heap - создать max/min кучу
def heap(_arr: list, *, _heap='max') -> None:
    # размер кучи
    _n = len(_arr)
    # цикл от первого индекса нелистового узла до 0
    for _i in range(_n//2 - 1, -1, -1):
        # создаем кучу по убыванию/возростанию
        heapify(_arr=_arr, _i=_i, _heap=_heap)

# heap_insert - вставка нового элемента в max/min кучу
def heap_insert (_arr: list, _value: int, *, _heap='max') -> None:
    # добавляем новое значение/узел в конец бинарной кучи
    _arr.append(_value)
    # создаем/обновляем max/min кучу
    heap(_arr=_arr, _heap=_heap)

# heap_increase_key -  заменяет элемент кучи на новый ключ со значением, 
# не меньшим/не большим значения исходного элемента
def heap_increase_key(_arr: list, _i: int, _key: int, *, _heap='max') -> None:
    """
    функция heap_increase_key - заменяет элемент кучи на новый ключ со значением\n
    не меньшим/не большим значения исходного элемента\n
    \t _arr - массив/куча\n
    \t _i - первый нелистовой узел, его индекс равен _n/2 - 1\n
    \t _key - новый ключ со значением\n
    \t _heap='max|min' - максимальный или минимальный начальный элемент кучи\n
    _i - индекс текущего узла\n
    _arr[_i] - текущий элемент массива - _current_element\n
    _n - размер массива (кучи)
    """
    # определяем вид кучи - по убыванию или возростанию
    if 'max' == _heap:
        ...
    else:
        ...
    # индекс кучи который необходимо обновить
    _arr[_i] = _key


# Heap_Increase_Key(A, i, key)
#   if key < A[i]
#     then error "Новый ключ меньше предыдущего"
#   A[i] ← key
#   while i > 1 и A[⌊i/2⌋] < A[i]
#     do Обменять A[i] ↔ A[⌊i/2⌋]
#       i ← ⌊i/2⌋


# Heap_Insert(A, key)
#   A.heap_size ← A.heap_size+1
#   A[A.heap_size] ← -∞
#   Heap_Increase_Key(A, A.heap_size, key)

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
    c1 = [3, 9, 2, 1, 4, 5]
    d1 = [3, 9, 2, 1, 4, 5]
    e = [3, 9, 2, 1, 4, 5]
    e1 = [3, 9, 2, 1, 4, 5]
    
    print('----------origin:--------')
    print(a)

    print('---------heapify max:----------')
    # heapify(b, (len(a)//2) - 1)
    print(b)
    # heapify(b, 0)
    heapify(b, 0, _heap='max')
    print(b)

    print('----------heap_max:----------')
    print(c)
    heap_max(c)
    print(c)

    print('----------heap_min:----------')
    print(d)
    heap_min(d)
    print(d)

    print('----------heap_max1:----------')
    print(c)
    heap(c, _heap='max')
    print(c)

    print('----------heap_min2:----------')
    print(d)
    heap(d, _heap='min')
    print(d)

    print('----------heap_insert-max:----------')
    print(e)
    heap_insert(e, 333, _heap='max')
    print(e)

    print('----------heap_insert-min:----------')
    print(e1)
    heap_insert(e1, 333, _heap='min')
    print(e1)