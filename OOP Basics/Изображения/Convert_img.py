import os.path
from PIL import Image

HOME = 'C:\\Temp'
EXT1 = 'png'
EXT2 = 'jpg'

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

def convert_img(ext_source, ext_result):
    files = dir_detail('.', True)
    for name in files:
        if name.endswith(ext_source):
            im = Image.open(name)
            root, ext = os.path.splitext(name)
            im.save(root + '.' + ext_result)

os.chdir(HOME)
convert_img(EXT1, EXT2)