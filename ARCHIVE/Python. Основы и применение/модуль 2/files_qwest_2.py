import os
import os.path

class File:
	def __init__(self):
		pass
		
def main():
	'''
	os.chdir('sample/')
	print(os.listdir())
	'''
	'''
	name_dir_list = list()
	dirs_list = list()
	files_list = list()
	'''
	
	name_dir_set = set()
	for name_dir, dirs, files in os.walk('main'):
		for word in files:
			if word.endswith('.py'):
				name_dir_set.add(name_dir)
		#name_dir_list.extend([name_dir])
		#dirs_list.extend(dirs)
		#files_list.extend(files)
	#print(name_dir_list)
	#print(dirs_list)
	#print(files_list)
	#print(name_dir_set)
	
	arr = list(name_dir_set)
	arr.sort()
	print('\n'.join(arr))
	
if __name__ == '__main__':
	main()