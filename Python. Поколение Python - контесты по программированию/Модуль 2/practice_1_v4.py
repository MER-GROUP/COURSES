# авторский алгоритм от BEEGIK
class Seq:
    def __init__(self, n) -> None:
        self.__algo(n)

    def __algo(self, na):
        n = na
        count_index, sum_count_index = 1, 0
        while sum_count_index + count_index <= n:
            print((str(count_index) + ' ') * count_index, end='')
            sum_count_index += count_index
            count_index += 1
        print((str(count_index) + ' ')  * (n - sum_count_index), end='') 

if __name__ == '__main__':
	Seq(int(input()))