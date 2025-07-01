from zipfile import ZipFile

def dimension(filename):
    size = filename.file_size
    if size < 1024:
        return f'{size} B'
    elif size < 1024 ** 2:
        return f'{int(round(size / 1024))} KB'
    elif size < 1024 ** 3:
        return f'{int(round(size / 1024 ** 2))} MB'
    else:
        return f'{int(round(size / 1024 ** 3))} GB'

with ZipFile('desktop.zip', 'r') as zip_file:
    info = zip_file.infolist()
    for item in info:
        if item.is_dir():
            rs = item.filename.rfind('/')
            ls = item.filename[:rs].rfind('/')
            name_dir = item.filename[ls + 1:rs]
            print(' ' * (item.filename.count('/') - 1) * 2 + name_dir)
        else:
            rs = item.filename.rfind('/')
            name_file = item.filename[rs + 1:]
            dimen = dimension(item)
            print(' ' * item.filename.count('/') * 2 + name_file + ' ' + dimen)