class Seq:
    def __init__(self, n) -> None:
        print(*self.__algo(n))

    def __algo(self, n):
        arr = list()
        for i in range(1, n + 1):
            arr += [i] * i
            if n <= len(arr):
                break
        return arr[: n]

    def __algo1(self, n):
        arr = list()
        i = 0
        while len(arr) < n:
            arr += [i] * i
            i += 1
        return arr[: n]

    def __algo2(self, n):
        num, count =  1, 0 
        for _ in range(int(input())):
            print(num, end=' ')
            count += 1
            if num == count:
                count = 0
                num += 1

    def __algo3(self, n):
        n = int(input())
        k = 1
        for i in range(1, n + 1, 1):
            print(k, end = " ")
            if (k * (k + 1) == 2 * i):
                k += 1

    def __algo4(self, n):
        arr = list()
        for i in range(1, n + 1):
            for _ in range(i):
                arr.append(i)
        return arr[: n]

if __name__ == '__main__':
	Seq(int(input()))