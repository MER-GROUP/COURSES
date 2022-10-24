class Compl:
	def __init__(self, n, z1, z2):
		print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n + 1))
		
if __name__ == '__main__':
	Compl(int(input()), complex(input()), complex(input()))