from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    cnt = 0
    for item in info:
        cnt += (not item.is_dir())
    print(cnt)