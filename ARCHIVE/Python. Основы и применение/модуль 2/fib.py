print(__name__)

def fib(x):
	if x in (0, 1):
		return 1
	else:
		return fib(x - 1) + fib(x - 2)
		
if __name__ == '__main__':
	print(fib(31))