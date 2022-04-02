for i in range(4):
	for j in range(17):
		if i==0 or i==3:
			print('*',end='')
			if 16==j:
				print()
		else:
			if 0==j:
				print('*',end='')
			elif 16==j:
				print('*')
			else:
				print(' ',end='')