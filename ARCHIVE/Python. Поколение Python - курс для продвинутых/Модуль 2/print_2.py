class ITM:
	def __init__(self, m, r):
		self.m = m
		self.r = r
		self.itm = float()
		self.__print__()
		
	def __itm__(self):
		return self.m / self.r ** 2
		
	def __print__(self):
		self.itm = self.__itm__()
		if 18.5 <= self.itm <= 25:
			print('Оптимальная масса')
		elif 18.5 > self.itm:
			print('Недостаточная масса')
		else:
			print('Избыточная масса')
			
if __name__ == '__main__':
	ITM(float(input()), float(input()))