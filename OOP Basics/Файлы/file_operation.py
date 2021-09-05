import os.path


def dir_detail(path, mode):
    if os.path.isdir(path):
        list_dirs = []
        list_files = []
        for root, dirs, files in os.walk(path):
            list_dirs += dirs
            list_files += files
        if mode:
            return list_files
        else:
            return list_dirs
    else:
        return []
         
def dir_clear(path):
    if os.path.isdir(path):
        list_dirs = dir_detail(path, False)
        if not list_dirs:
            list_files = dir_detail(path, True)
            for file in list_files:
                os.remove(path + '\\' + file)
            os.rmdir(path)
            return 1
        else:
            return -1
    else:
        return -2

def print_result (error_code, dir):
    if error_code == 1:
        print(f'Каталог {dir} удален')
    elif error_code == -1:
        print(f'Удаление каталога {dir} невозможно: каталог содержит подкаталоги')
    elif error_code == -2:
        print(f'Каталог {dir} не существует')

DIR1 = 'C:/Temp'
DIR2 = 'C:/Temp/1'


result = '\n'.join(dir_detail(DIR1, True))
print(result)
error_code = dir_clear(DIR1)
print_result(error_code, DIR1)

error_code = dir_clear(DIR2)
print_result(error_code, DIR2)