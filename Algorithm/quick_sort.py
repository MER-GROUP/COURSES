import random

# version 1
def quick_sort(arr: list) -> None:
    n = len(arr)
    if n <= 1:
        return arr
    else:
        num = random.choice(arr)
        lt_arr = []
        eq_arr = []
        gt_arr = []
        for el in arr:
            if el < num:
                lt_arr.append(el)
            elif el > num:
                gt_arr.append(el)
            else:
                eq_arr.append(el)
        return quick_sort(lt_arr) + eq_arr + quick_sort(gt_arr)

if __name__ == '__main__':
    from random import randint

    N = 10
    arr = [randint(1, 99) for item in range(N)]
    
    print(arr)
    # quick_sort(arr)
    print(quick_sort(arr))
    print(arr)

    print('-------------------------------')
    _arr = [1, 2, 3, 4, 5]
    print(_arr)
    print(random.choice(_arr))
    print(_arr)