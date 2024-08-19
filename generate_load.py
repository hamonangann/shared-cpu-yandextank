import csv
import math
import sys

address = sys.argv[1]

workload = []

# The CSV file must contains only one column without header
# Each row value is average CPU usage per fixed length of time
with open("./workload.csv", "r", encoding="utf-8-sig") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=",")
    for row in reader_variable:
        request_per_second = math.ceil(float(row[0])*2.0)
        workload.append(request_per_second)


with open('load.yaml', "w", encoding="utf-8") as f:
    f.write('phantom:\n')
    f.write('  address: ' + address + "\n")
    f.write('  uris:\n')
    f.write('    - /\n')

    f.write('  load_profile:\n')
    f.write('    load_type: rps\n')
    f.write('    schedule:')

    for w in workload:
        f.write(' const(' + str(w) + ', 15s)')
    f.write('\n')

    f.write('console:\n')
    f.write('  enabled: true\n')
    f.write('telegraf:\n')
    f.write('  enabled: true\n')
