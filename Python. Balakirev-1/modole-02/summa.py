import itertools as it

if __name__ == '__main__':
    perm = it.permutations('12345')
    # perm = it.permutations((1, 2, 3, 4, 5))

    # print(*perm)
    print(sum(map(lambda x: int(''.join(x)), perm)))

    # answer 3999960