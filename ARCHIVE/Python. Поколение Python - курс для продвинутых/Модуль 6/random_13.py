from random import shuffle

class Friend:
	def __init__(self, n):
		self.students = [input() for _ in range(n)]
		self.dictor = dict.fromkeys(self.students)
		self.__friend_set()
		self.print_dict()
		
	def print_dict(self):
		for k, v in self.dictor.items():
			print(f'{k} - {v}')
			
	def __friend_set(self):
		shuffle(self.students)
		for k in self.dictor.keys():
			if not k == self.students[0]:
				self.dictor[k] = self.students.pop(0)
			else:
				self.dictor[k] = self.students.pop(1)
		
if __name__ == '__main__':
	Friend(int(input()))