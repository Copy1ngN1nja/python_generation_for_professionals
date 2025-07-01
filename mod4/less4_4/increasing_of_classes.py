import csv

def key_sort(x):
    class_num, letter = x.split('-')
    return (int(class_num), letter)

with open('student_counts.csv', 'r') as input_file, open('sorted_student_counts.csv', 'w', newline='') as output_file:
    dict_reader = csv.DictReader(input_file)
    writer = csv.writer(output_file)
    
    header = dict_reader.fieldnames
    header = header[:1] + sorted(header[1:], key=key_sort)
    writer.writerow(header)
    for row in dict_reader:
        sorted_row = [row[key] for key in header]
        writer.writerow(sorted_row)

    