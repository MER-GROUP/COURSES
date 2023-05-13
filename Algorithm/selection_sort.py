# def selection_sort(arr: list) -> None:
#     i, n = 0, len(arr)
#     while i < n - 1:
#         min_index = i
#         j = i + 1
#         while j < n:
#             if arr[j] < arr[min_index]:
#                 min_index = j
#             j += 1
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         i += 1

def selection_sort(arr: list) -> None:
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    from random import randint

    N = 10
    arr = [randint(1, 99) for item in range(N)]
    
    print(arr)
    selection_sort(arr)
    print(arr)