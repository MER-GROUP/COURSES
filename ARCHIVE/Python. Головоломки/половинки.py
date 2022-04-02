s = input()
s1, s2 = int(), int()
if 0 == len(s) % 2:
	s1 = s[ : int(len(s) / 2)]
	s2 = s[int(len(s) / 2) : ]
else:
	s1 = s[ : len(s) // 2 + 1]
	s2 = s[len(s) // 2 + 1 : ]
#print(s1)
#print(s2)
print(s2+s1)

s = input()
pos = len(s) // 2
print(s[-pos : ] + s[ : -pos])

s = input()
pos = len(s) // 2 + len(s) % 2
print(s[pos : ] + s[ : pos])