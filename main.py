def write_in_txt_file():
	with open('test.txt', 'w') as writer:
		writer.write('I love Git')
		return True


if __name__ == "__main__":
	if write_in_txt_file(): # создаем и пишем в файл "I love Git"
		print("[OK] write")

	print(read_txt_file()) #читаем содержимое

	if delete_file(): #удаляем файл
		print("[OK] delete")
