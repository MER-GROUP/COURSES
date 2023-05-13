# def bubble_sort(arr: list) -> None:
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 buff = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = buff


# def bubble_sort(arr: list) -> None:
#     i, n = 0, len(arr)
#     while i < n - 1:
#         j = 0
#         while j < n - 1 - i:
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#             j += 1
#         i += 1

def bubble_sort(arr: list) -> None:
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

if __name__ == '__main__':
    from random import randint

    N = 10
    a = []
    for i in range(N):
        a.append(randint(1, 99))
    
    print(a)
    bubble_sort(a)
    print(a)