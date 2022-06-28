

import os

def delete_flie():
	file_path = 'file.txt'
	try:
		os.remove(file.path)
		return True
	except:
		print("The system cannot find the file specified")
		return False

def read_txt_file():
	file = 'file.txt'
with open(file, 'r', encoding='utf-8') as f:
	data = f.read()
	print(data)
	return data

def write_in_txt_file():
	with open('test.txt', 'w') as writer:
		writer.write('I love Git')
		return True


