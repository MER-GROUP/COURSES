from random import randint

class Search:
	def __init__(self):
		pass
		
	@staticmethod
	def binary_search(arr, el):
		mid = len(arr) // 2
		low, high = 0, len(arr) - 1
		while not arr[mid] == el and low <= high:
			if arr[mid] < el: low = mid + 1
			else: high = mid - 1
			mid = (low + high) // 2
		return None if low > high else mid
		
def main():
		arr = [randint(1, 20) for i in range(19)]
		arr.sort()
		print(arr)
		print(Search.binary_search(arr, int(input())))
		
if __name__ == '__main__':
	main()