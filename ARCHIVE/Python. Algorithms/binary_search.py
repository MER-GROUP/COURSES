# бинарный поиск
def binary_search(arr, el):
	mid = len(arr) // 2
	low, high = 0, len(arr) - 1
	while not arr[mid] == el and low <= high:
		if arr[mid] < el: low = mid + 1
		else: high = mid - 1
		mid = (low + high) // 2
	return None if low > high else mid
		
arr = [3, 6, 7, 7, 8, 9, 13, 13, 15, 18]
print(arr)
print(binary_search(arr, 10))
arr = [1, 8, 8, 10, 12, 13, 15, 18, 19, 19]
print(arr)
print(binary_search(arr, 18))