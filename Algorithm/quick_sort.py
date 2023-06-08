import random

# version 1
def quick_sort(arr: list) -> list:
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
    
# version 2
def quick_sort(arr: list) -> list:
    n = len(arr)
    if n <= 1:
        return arr
    else:
        num = random.choice(arr)
        lt_arr = [el for el in arr if el < num]
        eq_arr = [num] * arr.count(num)
        gt_arr = [el for el in arr if el > num] 
        return quick_sort(lt_arr) + eq_arr + quick_sort(gt_arr)
    
# version 3
def quick_sort(arr: list) -> None:
    def _quick_sort(_arr: list = arr, _left: int = 0, _right: int = len(arr)-1) -> None:
        if _left >= _right:
            return
        else:
            num = random.choice(_arr[_left : _right+1])
            _l = _left
            _r = _right
            while _l <= _r:
                while _arr[_l] < num:
                    _l += 1
                while _arr[_r] > num:
                    _r -= 1
                if _l <= _r: 
                    _arr[_l], _arr[_r] = _arr[_r], _arr[_l]
                    _l += 1
                    _r -= 1 
                    _quick_sort(_arr, _left, _r)
                    _quick_sort(_arr, _l, _right)
    _quick_sort()

if __name__ == '__main__':
    from random import randint

    N = 10
    arr = [randint(1, 99) for item in range(N)]
    
    print(arr)
    quick_sort(arr)
    print(arr)
    # print(quick_sort(arr))