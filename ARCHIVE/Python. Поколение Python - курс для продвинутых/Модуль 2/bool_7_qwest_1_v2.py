def func(num1, num2):
	return 'делится' if not bool(num1 % num2) else 'не делится'
	
if __name__ == '__main__':
	print(func(int(input()), int(input())))