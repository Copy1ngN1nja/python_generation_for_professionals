from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    sum_compressed_size = sum(item.compress_size for item in info if not item.is_dir())
    sum_file_size = sum(item.file_size for item in info if not item.is_dir())
    print(f'Объем исходных файлов: {sum_file_size} байт(а)')
    print(f'Объем сжатых файлов: {sum_compressed_size} байт(а)')