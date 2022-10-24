class MyDict:
	def __init__(self, n):
		self.curs = [{'CS101': ['3004', 'Хайнс', '8:00']}, {'CS102': ['4501', 'Альварадо', '9:00']}, {'CS103': ['6755', 'Рич', '10:00']}, {'NT110': ['1244', 'Берк', '11:00']}, {'CM241': ['1411', 'Ли', '13:00']}]
		self.__out(n.upper())
		
	def __out(self, n):
		for i in self.curs:
			if n == str(*i.keys()):
				print(f'{n}: {i[n][0]}, {i[n][1]}, {i[n][2]}')
				break
		
if __name__ == '__main__':
	MyDict(input())