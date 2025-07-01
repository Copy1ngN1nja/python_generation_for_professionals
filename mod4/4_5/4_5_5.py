from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = list(filter(lambda x: not x.is_dir(), zip_file.infolist()))
    info.sort(key=lambda x: (x.filename[x.filename.find('/') + 1:]))
    for item in info:
        print(item.filename[item.filename.find('/') + 1:])
        print(f'  Дата модификации файла: {item.date_time[0]:02d}-{item.date_time[1]:02d}-{item.date_time[2]:02d} \
{item.date_time[3]:02d}:{item.date_time[4]:02d}:{item.date_time[5]:02d}')
        print(f'  Объем исходного файла: {item.file_size} байт(а)')
        print(f'  Объем сжатого файла: {item.compress_size} байт(а)')
        print()
    