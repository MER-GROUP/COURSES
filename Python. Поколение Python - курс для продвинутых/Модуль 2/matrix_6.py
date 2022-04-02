if __name__ == '__main__':
	for _ in range(int(input())):
		arr = list(map(int, input().split()))
		av = sum(arr) / len(arr)
		cnt = int()
		for i in arr:
			if av < i:
				cnt += 1
		print(cnt)