import sys
import csv
import time

rooms = ['officeCarp','hallwayCarp','livingCarp','kitchenCarp','bedroomCarp','bathroomCarp']
activity_cols = ['Activity']
# time_cols = ['Time','timestamp']
FEATURE = 'Time'
time_cols = [FEATURE]

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
            data[FEATURE] = int(time.mktime(time.strptime(row[FEATURE], '%Y-%m-%d %H:%M:%S')))
            csvwr.writerow(data)

