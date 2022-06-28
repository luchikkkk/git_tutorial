
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

