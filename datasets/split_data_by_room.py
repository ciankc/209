import sys
import csv

rooms = ["officeCarp","livingCarp","kitchenCarp","bedroomCarp","bathroomCarp"]
activity_cols = ["Activity"]
time_cols = ["Time","timestamp"]

INFERENCE = False
prefix = ""
if INFERENCE:
    prefix = "inf-"

for room in rooms:
    fieldnames = list(time_cols)
    fieldnames.insert(0, room)   

    result = open(prefix + room + ".csv", "w")
    csvwr = csv.DictWriter(result, fieldnames=fieldnames)
    csvwr.writeheader()

    for file in sys.argv[1:]:
        nextfile = open(file)
        csvdr = csv.DictReader(nextfile)
        for row in csvdr:
            data = {}
            for field in fieldnames:
                data[field] = row[field]
            csvwr.writerow(data)

