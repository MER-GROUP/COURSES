txt = input()
print(sum(txt.count(i)//2 for i in set(txt)) * 2 + 1)