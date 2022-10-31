def gen_nums():
    i = k = 0  # число последовательности, длина подпоследовательности
    while True:
        k += 1
        for n in range(i + k, i, -1):
            yield n
        i += k

nums = gen_nums()
[print(next(nums), end=' ') for _ in range(int(input()))]