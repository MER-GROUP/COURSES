s = input()
lst = [s.count(i) for i in set(s)]
print(sum(i - i % 2 for i in lst) + any(i % 2 for i in lst))