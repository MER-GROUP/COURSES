from collections import Counter

letters = list(input())
max_polindrome = 1
for v in Counter(letters).values():
    max_polindrome += v if v % 2 == 0 else v-1
print(max_polindrome)