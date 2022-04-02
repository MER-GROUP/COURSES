class Digit:
	def __init__(self) -> None:
		pass
		
	@staticmethod
	def arr_enter(n: int) -> list:
		return (int(input()) for _ in range(n))
		
def main() -> None:
	n = int(input())
	arr = Digit.arr_enter(n)
	print(sum(arr))
	
if __name__ == '__main__':
	main()