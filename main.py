
import os

def delete_flie():
	file_path = 'file.txt'
	try:
		os.remove(file.path)
		return True
	except:
		print("The system cannot find the file specified")
		return False
