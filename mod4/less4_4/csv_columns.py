import csv


def csv_columns(csv_file):
    with open(csv_file, mode='r') as file:
        dict_reader = csv.DictReader(file, delimiter=',')
        result = {key: [] for key in dict_reader.fieldnames}
        for d in dict_reader:
            for key, value in d.items():
                result[key].append(value)
    return result


print(csv_columns('exam.csv'))