import requests

class File:
	def __init__(self) -> None:
		pass
		
	@staticmethod
	def file_open() -> str:
		s = str()
		with open('quest2.txt') as f:
			s = f.read().strip()
		return s
		
	@staticmethod
	def file_write(s: str) -> None:
		with open('quest2_ans.txt', 'w') as f:
			f.write(s)
		
	@staticmethod
	def tire() -> None:
		print('------------------------------')
		
class Request(File):
	@staticmethod
	def rec_end(s: str) -> list:
		count = int(1)
		while True:
			url = 'https://stepic.org/media/attachments/course67/3.6.3/'
			word = s.split('/')
			#print(url + word[-1].strip())
			req = requests.get(url + word[-1].strip())
			print(count)
			count += 1
			print(req.text)
			arr = req.text.strip().split()
			if 'we' == arr[0].lower():
				return req.text
			s = req.text
	
def main() -> None:
	file = Request.file_open()
	print(file)
	Request.tire()
	url = Request.rec_end(file)
	#print(url)
	Request.file_write(url)
	
if __name__ == '__main__':
	main()