import csv
import sys
import struct

with open(sys.argv[1], "r") as csv_file, open(sys.argv[2], "wb") as raw_file:
    for i in range(3):
        print(csv_file.readline())
    reader = csv.reader(csv_file, delimiter='\t')
    for row in reader:
        raw_file.write(struct.pack("f", float(row[1])))
