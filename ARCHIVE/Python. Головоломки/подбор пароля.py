# put your python code here
#вывести abc,acb,bac,bca,cab,cba
'''
cso=int(input())
a=cso%10
b=(cso//10)%10
c=cso//100
buf=str(a)+str(b)+str(c)
buf=''.join(reversed(buf))
print(type(buf))
'''
buf = input()
print('Подбор паролей : ')

#перебор всех ввриантов
for i in buf:
	for j in buf:
		for k in buf:
			print(i, j, k, sep='')

print('Подбор паролей по условию : ')
#перебор по условию
for i in buf:
	for j in buf:
		for k in buf:
			if i != j and j != k and k != i:
				print(i, j, k, sep='')