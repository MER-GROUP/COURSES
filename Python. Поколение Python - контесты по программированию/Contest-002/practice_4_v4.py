start_str = input()
sample = ''
total = 0
for i in start_str:
    if i not in sample:
        sample += i
        total += start_str.count(i) // 2
print(total * 2 + 1)