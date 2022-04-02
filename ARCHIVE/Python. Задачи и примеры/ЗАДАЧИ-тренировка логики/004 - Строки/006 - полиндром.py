def Polindrom(s):
	check = True
	#for i in range(int(len(s) / 2)):
	for i in range(len(s) // 2):
		if not s[i] == s[-1 - i]:
			print("It's not Polindrom")
			check = False
			break
	if check:
		print("It's Polindrom")

def Main():
	while True:
		print('---Main---')
		s = input('Enter str : ')
		if 'q' == s:
			break
		else:
			Polindrom(s)
	
Main()