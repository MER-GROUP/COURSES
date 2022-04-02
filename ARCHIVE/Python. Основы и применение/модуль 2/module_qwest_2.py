# пример работы с simple-crypt и методом simplecrypt.decrypt
# pip install simple-crypt
# sudo pip install simple-crypt

import simplecrypt

class File:
	def __init__(self):
		pass
		
	def file_read_bin(self):
		with open('encrypted.bin', 'rb') as fb:
			return fb.read()
			
	def file_read(self):
		with open('passwords.txt', 'r') as f:
			return f.readlines()
		
def main():
	file_pswd, file = [File()] * 2
	password = file_pswd.file_read()
	crypted = file.file_read_bin()
	
	idx = int()
	while True:
		try:
			print(password[idx], ' #', idx + 1)
			encrypted = simplecrypt.decrypt(password[idx].strip(), crypted)
		except simplecrypt.DecryptionException:
			print(password[idx], ' error password')
			idx += 1
		else:
			print(encrypted)
			break
	
if __name__ == '__main__':
	main()