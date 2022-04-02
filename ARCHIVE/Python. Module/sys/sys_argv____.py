from sys import argv

class Console:
	def __init__(self) -> None:
		pass
		
	@staticmethod
	def info_argv() -> None:
		if 1 < len(argv):
			print(*argv[1 : ])
		
def main() -> None:
	Console.info_argv()
	
if __name__ == '__main__':
	main()