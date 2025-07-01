import csv, json

with open('students.json', 'r') as input_file, open('data.csv', 'w', newline='') as output_file:
    data = json.load(input_file)
    writer = csv.writer(output_file, delimiter=',')
    good_students = []
    for student in data:
        if student['progress'] >= 75 and student['age'] >= 18:
            good_students.append((student['name'], student['phone']))
    good_students.sort(key=lambda x: x[0])
    writer.writerow(['name', 'phone'])
    writer.writerows(good_students)

    