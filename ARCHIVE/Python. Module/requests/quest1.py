import requests

class File:
	def __init__(self) -> None:
		pass
		
	@staticmethod
	def file_read() -> str:
		s = str()
		with open('quest1.txt') as f:
			s = f.read().strip()
		return s
		
	@staticmethod
	def file_readlines() -> list:
		arr = list()
		with open('quest1_ans.txt') as f:
			arr = f.readlines()
		return arr
		
	@staticmethod
	def file_write(s: str) -> None:
		with open('quest1_ans.txt', 'w') as f:
			f.write(s)
			
	@staticmethod
	def file_count_str(arr: list) -> int:
		return len(arr)
		
	@staticmethod
	def file_count_str_2(s: str) -> int:
		arr = s.splitlines()
		return len(arr)
		
	@staticmethod
	def tire() -> None:
		print('------------------------------')
		
class Request(File):
	@staticmethod
	def page_get(url) -> str:
		req = requests.get(url)
		return req.text
		
def main() -> None:
	#url_file = File.file_read()
	url_file = Request.file_read()
	#print(type(url_file))
	print(url_file)
	Request.tire()
	page = Request.page_get(url_file)
	#print(type(page.text))
	#print(type(page))
	#print(*page)
	#print(page.text)
	#print(page)
	Request.file_write(page)
	file = Request.file_readlines()
	#print(file)
	print(Request.file_count_str(file))
	print(Request.file_count_str_2(page))
	
if __name__ == '__main__':
	main()