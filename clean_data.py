import csv
import sys

f = open("files/data.csv", "rt")
reader = csv.reader(f)
w = csv.writer(sys.stdout)
found_invalid = False
for row in reader:
    for col in row:
        if (col == '?'):
            found_invalid = True