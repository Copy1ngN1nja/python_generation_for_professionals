import csv

def condence_csv(input_file_path, id_name):
    with open(input_file_path, 'r') as input_file, open('condensed.csv', 'w') as output_file:
        reader = csv.reader(input_file, delimiter=',')
        res_d = {}
        headers = []
        for row in reader:
            name, title, title_value = row[0], row[1], row[2]
            if name not in res_d:
                res_d[name] = {id_name: name}
            if title not in headers:
                headers.append(title)
            res_d[name][title] = title_value
        writer = csv.writer(output_file, delimiter=',')
        writer.writerow([id_name] + headers)
        for name, name_data in res_d.items():
            writer.writerow([name] + [name_data[header] for header in headers])



condence_csv('data.csv', id_name='ID')