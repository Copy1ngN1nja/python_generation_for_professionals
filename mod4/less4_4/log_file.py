import csv
from datetime import datetime


with open('name_log.csv', 'r') as input_file, open('new_name_log.csv', 'w') as output_file:
    dict_reader = csv.DictReader(input_file, delimiter=',')
    dict_writer = csv.writer(output_file, delimiter=',')
    time_of_write = {}
    nicks = {}
    for d in dict_reader:
        email = d['email']
        time = datetime.strptime(d['dtime'], '%d/%m/%Y %H:%M')
        if email not in time_of_write or time_of_write[email] < time:
            time_of_write[email] = time
            nicks[email] = d['username']
    dict_writer.writerow(['username', 'email', 'dtime'])
    for email, dtime in sorted(time_of_write.items(), key=lambda x: x[0]):
        dict_writer.writerow([nicks[email], email, dtime.strftime('%d/%m/%Y %H:%M')])

