import csv, json
from datetime import datetime


with open('exam_results.csv', 'r') as csv_file, open('best_scores.json', 'w') as json_file:
    csv_reader = csv.DictReader(csv_file)
    email_to_index = {}
    best_tries = []
    for row in csv_reader:
        email = row['email']
        if email not in email_to_index:
            email_to_index[email] = len(email_to_index)
            best_tries.append(row)
        last_best_try = best_tries[email_to_index[email]]
        last_best_try_datetime = datetime.strptime(last_best_try['date_and_time'], '%Y-%m-%d %H:%M:%S')
        row_datetime = datetime.strptime(row['date_and_time'], '%Y-%m-%d %H:%M:%S')
        if last_best_try['score'] < row['score'] or (last_best_try['score'] == row['score'] and last_best_try_datetime < row_datetime):
            best_tries[email_to_index[email]] = row
    best_tries.sort(key=lambda x: x['email'])
    for i in range(len(best_tries)):
        best_tries[i]['best_score'] = best_tries[i].pop('score')
        best_tries[i]['best_score'] = int(best_tries[i]['best_score'])
    json.dump(best_tries, json_file, indent=3)
        
