def Chislo(s):
	num = str()
	for i in s:
		if i.isdigit():
			num += i
			continue
		else:
			if num.isdigit():
				print(num)
				num = str()
	if num.isdigit():
		print(num)

def Main():
	while True:
		print('---Main---')
		s = input()
		if 'q' == s:
			break
		Chislo(s)
	
Main()