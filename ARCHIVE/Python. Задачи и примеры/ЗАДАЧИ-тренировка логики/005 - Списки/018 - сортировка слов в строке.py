def SortStr(s):
	arr = s.split()
	arr.sort(key=len)
	s = ' '.join(arr)
	return s

def Main():
	for _ in range(5):
		print('---Main---')
		s = input('Введи слова : ')
		if 'q' == s:
			break
		print(SortStr(s))
		
Main()