n = input()
max_subst = 1
for i in range(1, len(n) // 2 + 1):
    if not len(n) % i:
        substrs = n.count(n[:i])
        if substrs * i == len(n) and max_subst < substrs:
            max_subst = substrs
print(max_subst)