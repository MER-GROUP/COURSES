class Com:
	def __init__(self, z1, z2):
		[print(f'{z1} {i} {z2} =', eval(f'{z1}{i}{z2}')) for i in '+-*']
		
if __name__ == '__main__':
	Com(complex(input()), complex(input()))