"""
Поиск всех файлов в заданном каталоге, включая файлы,
расположенные в подкаталогах произвольной вложенности
"""
import os.path

def get_filenames (root: str):
    """Init file search"""
    files = []
    return len(into_dir(root, files))

def into_dir(root: str, files: list):
    """Return filenames in the directory"""
    data = os.listdir(root)
    for i in data:
        if os.path.isfile(root + '/' + i):
            files.append(i)
        else:
            files = into_dir(root + '/' + i, files)
    return files
