#!/usr/bin/env python

import sys
import csv

results = []
with open(sys.argv[1], mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        row['address']+= sys.argv[2]
        results.append(row)
print(results)