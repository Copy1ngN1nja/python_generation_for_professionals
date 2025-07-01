from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if len(args) == 0:
            zip_file.extractall()
            return
        for file_name in args:
            zip_file.extract(file_name)

extract_this('workbook.zip')