from zipfile import ZipFile 
import os.path

HOME = 'C:\\Temp'
EXT = 'txt'
zip_name = 'VERY_IMPORTANT.zip'

def dir_detail(path, mode):
    if os.path.isdir(path):
        list_dirs = []
        list_files = []
        for root, dirs, files in os.walk(path):
            for name in files:
                list_files.append(root + '\\' + name)
            for name in dirs:
                list_dirs.append(root + '\\' + name)
        if mode:
            return list_files
        else:
            return list_dirs
    else:
        return []

def pack(zip_name, ext):
    with ZipFile(zip_name, 'w') as my_zip:
        files = dir_detail(HOME, True)
        for file in files:
            if file.endswith(EXT):
                my_zip.write(file)


os.chdir(HOME)
pack(zip_name, EXT)
