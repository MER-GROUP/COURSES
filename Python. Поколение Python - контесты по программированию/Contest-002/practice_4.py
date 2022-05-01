class Algo:
    def __init__(self, s) -> None:
        self.__algo(s)

    def __algo(self, s):
        arr = list(s)
        max = 0
        tmp_arr = list()
        for i in range(len(arr)):
            tmp_arr = arr[: i]
            for j in range(len(tmp_arr)):
                pass

if __name__ == '__main__':
    Algo(input())