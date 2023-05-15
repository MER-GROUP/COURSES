def insert_sort(arr: list) -> None:
    pass

if __name__ == '__main__':
    from random import randint

    N = 10
    arr = [randint(1, 99) for item in range(N)]
    
    print(arr)
    insert_sort(arr)
    print(arr)