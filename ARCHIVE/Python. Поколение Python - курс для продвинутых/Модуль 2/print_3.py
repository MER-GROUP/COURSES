class TXT:
	def __init__(self, txt):
		self.txt = txt
		self.__txt__()
		
	def __txt__(self):
		cnt = len(self.txt)
		cnt = 60 * cnt
		r, k = divmod(cnt, 100)
		print(r, 'р.', k, 'коп.')
		
if __name__ == '__main__':
	TXT(input())