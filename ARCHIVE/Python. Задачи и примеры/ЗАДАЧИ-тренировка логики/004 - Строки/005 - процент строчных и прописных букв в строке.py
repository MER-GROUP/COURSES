def Schet(s):
	lower, upper = 0, 0
	for i in s:
		if i.isupper():
			upper += 1
		elif i.islower():
			lower += 1
	perLower = lower / len(s) * 100
	perUpper = upper / len(s) * 100
	print(f'{perLower:.2f}')
	print(f'{perUpper:.2f}')

def Main():
	while True:
		print('---Main---')
		s = input()
		if 'q' == s:
			break
		Schet(s)
	
Main()