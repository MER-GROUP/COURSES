i=1
while 10>i:
	j=1
	while 10>j:
		#print(i*j,end='')
		print(f'{i*j:4d}',end='')
		j+=1
	i+=1
	print()
	
print()
i=1
while 10>i:
	j=1
	while 10>j:
		print('%4d'%(i*j),end='')
		j+=1
	i+=1
	print()

print()
i=1
while 10>i:
	j=1
	while 10>j:
		print('{0:4d}'.format(i*j),end='')
		j+=1
	i+=1
	print()
	
print()
i=1
while 10>i:
	j=1
	while 10>j:
		print('{chi:4d}'.format(chi=i*j),end='')
		j+=1
	i+=1
	print()