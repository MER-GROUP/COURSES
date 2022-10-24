def func(num1, num2):
	return 0 == num1 % num2
	
if __name__ == '__main__':
	num1, num2 = [int(input()) for _ in range(2)]
	if func(num1, num2):
		print('делится')
	else:
		print('не делится')