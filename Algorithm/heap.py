def heapify(arr: list) -> None:
    pass

if __name__ == '__main__':
    from random import randint

    N = 10
    a = []
    for i in range(N):
        a.append(randint(1, 99))
    
    print(a)
    heapify(a)
    print(a)