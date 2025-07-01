from zipfile import ZipFile

with ZipFile('test.zip', 'r') as zip_file:
    info = zip_file.infolist()
    print(*info, sep='\n')
