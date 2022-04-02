separator = ('.', ',', ':', ';', '!', '?', '(', ')')

def Algo(s):
	s = s.split()
	i = int()
	global separator
	for iter in s:
		if iter[-1] in separator:
			s[i] = iter[ : -1]
			iter = s[i]
		if iter[0] in separator:
			s[i] = iter[1 : ]
		i += 1
	return s
	
def Output(s):
	for i in s:
		print(i, end=' ')
	print()

def Main():
	while True:
		print('---Main---')
		s = input()
		if 'q' == s:
			break
		else:
			Output(Algo(s))
		
Main()