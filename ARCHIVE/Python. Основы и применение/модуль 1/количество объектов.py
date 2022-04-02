print(1 == True)
print(1 is not True)
print([1, 2, 3] is not [1, 2, 3])
print([1, 2, 3] == [1, 2, 3])

objects = [1, 2, 0, 3, 4, 1, True, True, False, [True], None, [None, 1, True], {None}, {1: None}, [False, 1], {345}, {345}, 1, [2], 1, [2], 3, bin(1), bin(3), '0b1', '0b11', 0b11, 0b1]

ans = list()
for obj in objects:
    ans.append(id(obj))

print(len(set(ans)))