class Algo:
    def __init__(self, n) -> None:
        self.__algo(n)

    def __algo(self, n):
        arr = list()
        i = int(1)
        step = int(1)
        while len(arr) < n:
            j = i
            tmp_arr = list()
            while 0 < j:
                tmp_arr.append(step)
                step += 1
                j -= 1
            arr.extend(reversed(tmp_arr))
            i += 1
        print(*arr[: n])

if __name__ == '__main__':
    Algo(int(input()))