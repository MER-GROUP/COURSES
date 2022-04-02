class Com:
	def __init__(self, z1, z2):
		z1 = complex(z1)
		z2 = complex(z2)
		print(f'{z1} + {z2} = {z1 + z2}')
		print(f'{z1} - {z2} = {z1 - z2}')
		print(f'{z1} * {z2} = {z1 * z2}')
		
if __name__ == '__main__':
	Com(input(), input())