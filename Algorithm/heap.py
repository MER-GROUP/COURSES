###############################################################################################
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
###############################################################################################
# heap_max - создать max кучу
def heap_max(_arr: list) -> None:
    # размер кучи
    _n = len(_arr)
    # цикл от первого индекса нелистового узла до 0
    for _i in range(_n//2 - 1, -1, -1):
        # создаем кучу по убыванию
        heapify(_arr=_arr, _i=_i, _heap='max')
###############################################################################################
# heap_min - создать min кучу
def heap_min(_arr: list) -> None:
    # размер кучи
    _n = len(_arr)
    # цикл от первого индекса нелистового узла до 0
    for _i in range(_n//2 - 1, -1, -1):
        # создаем кучу по возростанию
        heapify(_arr=_arr, _i=_i, _heap='min')
###############################################################################################
# heap - создать max/min кучу
def heap(_arr: list, *, _heap='max') -> None:
    # размер кучи
    _n = len(_arr)
    # цикл от первого индекса нелистового узла до 0
    for _i in range(_n//2 - 1, -1, -1):
        # создаем кучу по убыванию/возростанию
        heapify(_arr=_arr, _i=_i, _heap=_heap)
###############################################################################################
# heap_insert - вставка нового элемента в max/min кучу
def heap_insert (_arr: list, _value: int, *, _heap='max') -> None:
    # добавляем новое значение/узел в конец бинарной кучи
    _arr.append(_value)
    # создаем/обновляем max/min кучу
    heap(_arr=_arr, _heap=_heap)
###############################################################################################
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
    _i - индекс текущего узла (обновляемого элемента)\n
    _arr[_i] - текущий элемент массива - _current_element\n
    _n - размер массива (кучи)
    """
    # пользовательское исключение на функцию heap_increase_key
    class heap_increase_key_error(Exception):
        pass

    # определяем вид кучи - по убыванию или возростанию
    if 'max' == _heap:
        # если новый элемент меньше текущего родителя
        # то он может оказаться и меньше своего сына
        # что недопустимо в max куче
        if _key < _arr[_i]:
            raise heap_increase_key_error(
                'a key must be greater or equal to the current'
            )
        # индекс кучи который необходимо обновить
        _arr[_i] = _key
        # покуда индекс обновленного элемента (сын) больше 1
        # и обновленный элемент (сын) больше родителя (элемента с индексом _i//2) 
        while _i > 0 and _arr[_i//2] < _arr[_i]:
            # меняем местами сына и родителя
            # если индекс родителя равен 1 то заменяем его на 0
            # а так постоянно делим на 2 без остатка
            _son = _i
            _parent = (0, _i//2)[1 < _i//2]
            _arr[_son], _arr[_parent] = _arr[_parent], _arr[_son]
            # обновляем индекс сына
            _i = _parent
    else:
        # если новый элемент больше текущего родителя
        # то он может оказаться и больше своего сына
        # что недопустимо в min куче
        if _key > _arr[_i]:
            raise heap_increase_key_error(
                'a key must be less or equal to the current'
            )
        # индекс кучи который необходимо обновить
        _arr[_i] = _key
        # покуда индекс обновленного элемента (сын) больше 1
        # и обновленный элемент (сын) меньше родителя (элемента с индексом _i//2) 
        while _i > 0 and _arr[_i//2] > _arr[_i]:
            # меняем местами сына и родителя
            # если индекс родителя равен 1 то заменяем его на 0
            # а так постоянно делим на 2 без остатка
            _son = _i
            _parent = (0, _i//2)[1 < _i//2]
            _arr[_son], _arr[_parent] = _arr[_parent], _arr[_son]
            # обновляем индекс сына
            _i = _parent
###############################################################################################
# heap_insert_increase - вставка нового элемента в max/min кучу через увеличение
def heap_insert_increase (_arr: list, _value: int, *, _heap='max') -> None:
    # добавляем новое значение/узел в конец бинарной кучи
    _arr.append(_value)
    # создаем/обновляем max/min кучу через увеличение
    heap_increase_key(_arr=_arr, _i=len(_arr)-1, _key=_value, _heap=_heap)
###############################################################################################
# heap_remove - удаление указанного элемента в max/min куче
def heap_remove (_arr: list, _value: int, *, _heap='max') -> None:
    # индекс удаляемого элемента
    _index_current = _arr.index(_value)
    # последний индекс кучи
    _index_last = len(_arr)-1
    # меняем местами значения текущего индекса (индекс значения который хотим удалить)
    # cо значением последнего индекса
    _arr[_index_current], _arr[_index_last] = _arr[_index_last], _arr[_index_current]
    # удаляем последний элемент кучи
    _arr.pop()
    
    # определяем вид кучи - по убыванию или возростанию
    if 'max' == _heap:
        # обновляем max-кучу
        heapify(_arr=_arr, _i=_index_current, _heap='max')
    else:
        # обновляем min-кучу
        heapify(_arr=_arr, _i=_index_current, _heap='min')
###############################################################################################
# heap_peek - возвращает максимальный/минимальный элемент из max/min кучи без удаления узла
def heap_peek (_arr: list) -> object:
    # возвращаем максимальный/минимальный элемент из max/min кучи без удаления узла
    return _arr[0]
###############################################################################################
# heap_extract_peek - извлекает максимальный/минимальный элемент 
# из max/min кучи c удалением узла
def heap_extract_peek(_arr: list) -> object:
    # пользовательское исключение на функцию heap_extract_peek
    class heap_extract_peek_error(Exception):
        pass

    # если куча пуста то кидаем исключение (выводим ошибку)
    if not _arr:
        raise heap_extract_peek_error(
                'a key must be greater or equal to the current'
            )
    
    ...
###############################################################################################
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

    print('----------heap_increase_key Exception for max:----------')
    print(e)
    # heap_increase_key(e, _i=1, _key=8, _heap='max')
    print(e)

    print('----------heap_increase_key Exception for min:----------')
    print(e1)
    # heap_increase_key(e1, _i=1, _key=5, _heap='min')
    print(e1)

    print('----------heap_increase_key for max:----------')
    print(e)
    # heap_increase_key(e, _i=5, _key=8, _heap='max')
    heap_increase_key(e, _i=5, _key=888, _heap='max')
    print(e)

    print('----------heap_increase_key for min:----------')
    print(e1)
    heap_increase_key(e1, _i=5, _key=1, _heap='min')
    print(e1)

    print('----------heap_insert_increase for max:----------')
    print(e)
    heap_insert_increase(e, _value=3, _heap='max')
    print(e)

    print('----------heap_insert_increase for min:----------')
    print(e1)
    heap_insert_increase(e1, _value=5, _heap='min')
    print(e1)

    print('----------heap_remove for max:----------')
    print(e)
    heap_remove(e, _value=9, _heap='max')
    print(e)

    print('----------heap_remove for min:----------')
    print(e1)
    heap_remove(e1, _value=1, _heap='min')
    print(e1)

    print('----------heap_peek for max:----------')
    print(e)
    print(heap_peek(e))
    print(e)

    print('----------heap_peek for min:----------')
    print(e1)
    print(heap_peek(e1))
    print(e1)
###############################################################################################