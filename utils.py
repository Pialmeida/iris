import os

def rename_files():
	path = os.path.join(os.path.dirname(__file__),'Input_database')
	for _dir in os.listdir(path):
		print(_dir)
		for i,x in enumerate(os.listdir(os.path.join(path,_dir))):
			old_name = os.path.join(path,_dir,x)
			new_name = os.path.join(path,_dir,f'{_dir}_{i}.jpg')
			os.rename(old_name,new_name)


if __name__ == '__main__':
	rename_files()