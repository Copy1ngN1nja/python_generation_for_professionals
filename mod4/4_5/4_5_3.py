from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    ans_idx = 0
    for i in range(len(info)):
        if not info[i].is_dir() and (ans_idx == 0 or info[i].compress_size / info[i].file_size < info[ans_idx].compress_size / info[ans_idx].file_size):
            ans_idx = i
    print(info[ans_idx].filename[info[ans_idx].filename.find('/') + 1:])