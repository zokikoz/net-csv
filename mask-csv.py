#!/usr/bin/env python
# Add mask to address row

import sys
import csv

results = []
with open(sys.argv[1], mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        row['address'] += sys.argv[2]
        results.append(row)
new_file = sys.argv[1] + '.mod'
with open(new_file, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, results[0].keys())
    csv_writer.writeheader()
    for row in results:
        csv_writer.writerow(row)
