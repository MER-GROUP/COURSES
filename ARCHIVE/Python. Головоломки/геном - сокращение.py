class Genom:
	def __init__(self):
		pass
		
	@staticmethod
	def __zip__(s):
		return s[0] + str(len(s))
		
	@staticmethod
	def to_arhiv(s):
		res, tmp = [str()] * 2
		i = int()
		while i < len(s):
			tmp = s[i]
			if not i + 1 == len(s):
				for j in range(i + 1, len(s)):
					if s[i] == s[j]:
						tmp += s[j]
						if j + 1 == len(s):
							i = j + 1
					else:
						i = j
						break
			else:
				i += 1
			res += Genom.__zip__(tmp)
			tmp = str()
		return res
		
	@staticmethod
	def to_arhiv2(s):
		res = str()
		cnt = int(1)
		for i in range(len(s) - 1):
			if s[i] == s[i + 1]:
				cnt += 1
			elif not s[i] == s[i + 1]:
				res += s[i] + str(cnt)
				cnt = int(1)
		res += s[-1] + str(cnt)
		return res
			
			
		
def main():
	print(Genom.to_arhiv(input()))
	print(Genom.to_arhiv2(input()))
	
if __name__ == '__main__':
	main()