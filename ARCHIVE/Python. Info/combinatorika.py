import itertools as it

# seq = [1, 2, 3, 4, 6]
seq = '12346'

# for i in it.accumulate(seq):
	
check = False
for i in it.permutations(seq):
	for j in it.accumulate(i):
		x = sum(map(int, j))
		y = sum(map(int, i[len(j) :]))
		print('x = ', x)
		print('y = ', y)
		print(j)
	print(i)