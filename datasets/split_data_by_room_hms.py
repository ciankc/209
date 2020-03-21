import sys
import csv
from datetime import datetime

rooms = ['officeCarp','hallwayCarp','livingCarp','kitchenCarp','bedroomCarp','bathroomCarp']
activity_cols = ['Activity']
# time_cols = ['Time','timestamp']
time_cols = ['timestamp']

INFERENCE = False
prefix = ''
if INFERENCE:
    prefix = 'inf-'

for room in rooms:
    fieldnames = list(time_cols)
    fieldnames.insert(0, room)   

    result = open(prefix + room + '.csv', 'w')
    csvwr = csv.DictWriter(result, fieldnames=fieldnames)
    csvwr.writeheader()

    for file in sys.argv[1:]:
        nextfile = open(file)
        csvdr = csv.DictReader(nextfile)
        for row in csvdr:
            data = {}
            data[room] = row[room]
            t = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
            t_int = t.hour * 3600 + t.minute * 60 + t.second
            data['timestamp'] = t_int
            csvwr.writerow(data)

