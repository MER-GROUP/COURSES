class Programmist:
	def __init__(self):
		pass
	@staticmethod
	def coint_progs(d):
		res = str()
		if 0 == d:
			res = str(d) + ' ' + 'программистов'
		elif 1 == d % 10 and not 11 == d % 100: 
			res = str(d) + ' ' + 'программист'
		elif 2 <= d % 10 <= 4 and not 12 <= d % 100 <= 14:
			res = str(d) + ' ' + 'программиста'
		else:
			res = str(d) + ' ' + 'программистов'
		return res
		
def main():
	print(Programmist.coint_progs(int(input())))
	
if __name__ == '__main__':
	main()