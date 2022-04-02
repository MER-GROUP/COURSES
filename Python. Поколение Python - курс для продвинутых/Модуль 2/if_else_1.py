class Coordinate:
	def __init__(self):
		self.x = int()
		self.y = int()
		self.res = {'Первая четверть:': 0, 'Вторая четверть:': 0, 'Третья четверть:': 0, 'Четвертая четверть:': 0}
		
	def coordinate(self, x, y):
		if 0 < x and 0 < y:
			self.res['Первая четверть:'] += 1
		elif 0 > x and 0 < y:
			self.res['Вторая четверть:'] += 1
		elif 0 > x and 0 > y:
			self.res['Третья четверть:'] += 1
		elif 0 < x and 0 > y:
			self.res['Четвертая четверть:'] += 1
			
	def print(self):
		for k, v in self.res.items():
			print(k, v)
		
def iterator(arr):
	coord = Coordinate()
	for i in range(len(arr)):
		coord.x =arr[i][0]
		coord.y =arr[i][1]
		coord.coordinate(coord.x, coord.y)
	coord.print()

if __name__ == '__main__':
	points = int(input())
	arr = list()
	for _ in range(points):
		x, y = input().split()
		tmp = [int(x), int(y)]
		arr.append(tmp.copy())
		tmp.clear()
	#print(arr)###
	iterator(arr)