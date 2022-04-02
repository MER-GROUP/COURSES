class Scrabble:
	def __init__(self, s):
		self.dictor = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'], 4: ['F', 'H', 'V', 'W', 'Y'], 5: ['K'], 8: ['J', 'X'], 10: ['Q', 'Z']}
		print(self.__game(s))
		
	def __game(self, s):
		return sum([k for c in s for k, v in self.dictor.items() if c in v])
		
if __name__ == '__main__':
	Scrabble(input())