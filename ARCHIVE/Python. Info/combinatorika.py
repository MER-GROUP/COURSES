import itertools as it

seq = [1, 2, 3, 4, 6]
# seq = [4,2,5,2,7,3,9,3,6,2,3,43,1,44,123,1]
# seq = '12346'
# seq = '46''

# for i in it.accumulate(seq):
	
check = False
for i in it.permutations(''.join(map(str,seq))):
	for j in it.accumulate(i):
		x = sum(map(int, j))
		y = sum(map(int, i[len(j) :]))
		print('x = ', x)
		print('y = ', y)
		if (x == y):
			print('True')
			check = True
			break
		# print(j)
	# print(i)
	if check: break
else: print('False')