s = input()
if 0 == s.count('f'):
	print(-2)
elif 1 == s.count('f'):
	print(-1)
else:
	start = s.find('f') + 1
	print(s.find('f', start, len(s)))