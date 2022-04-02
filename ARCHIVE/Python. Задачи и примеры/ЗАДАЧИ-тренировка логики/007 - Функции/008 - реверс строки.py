class Stroka:
	def __init__(self):
		pass
		
	@staticmethod
	def rev(s):
		res = s.split()
		res.reverse()
		return ' '.join(res)
		
def main():
		print(Stroka.rev(input()))
		
if __name__ == '__main__':
	main()