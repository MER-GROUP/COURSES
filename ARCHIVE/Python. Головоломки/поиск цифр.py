s = input()
for i in range(10):
	if not -1 == s.find(str(i)):
		print('Цифра')
		break
else:
	print('Цифр нет')