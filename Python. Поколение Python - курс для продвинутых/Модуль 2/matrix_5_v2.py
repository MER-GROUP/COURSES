if __name__ == '__main__':
	res = int()
	for i in range(int(input())):
		res += int(input().split()[i])
	print(res)