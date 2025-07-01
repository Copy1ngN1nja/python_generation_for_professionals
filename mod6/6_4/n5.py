import csv, datetime
from collections import namedtuple

with open('meetings.csv', 'r') as meetings_file:
    reader = csv.DictReader(meetings_file, delimiter=',')
    Person = namedtuple('Person', ['surname', 'name', 'datetime'])
    people = []
    for row in reader:
        person = Person(surname=row['surname'], name=row['name'], datetime=datetime.datetime.strptime(row['meeting_date'] + ' ' + row['meeting_time'], '%d.%m.%Y %H:%M'))
        people.append(person)
    people.sort(key=lambda p: p.datetime)
    for person in people:
        print(person.surname, person.name)

    