#!/usr/bin/env python3
import csv
import sys
import re

args = len(sys.argv)
if args>1:
    filename = str(sys.argv[1])
else:
    filename = str(input("Filename for trades dataset: "))

bt_file = 'bigtable_' + filename
csv_path = "./csv_files/"
bt_path = csv_path + "bigtable_trades/"
tally_file = "tally.csv"

#['date', 'span', 'vol_0', 'vol_1', 'vol_2']

x = re.search(r"[0-9]{8}-[0-9]*", filename)
date = x[0][0:8]
span = re.search(r"[0-9]*$", x[0])
span = span[0]
count0 = 0
count1 = 0
count2 = 0

with open(bt_path + bt_file, 'r', newline='') as bigtable:
    bt_read = csv.reader(bigtable)
    bt_header = next(bt_read)
    index_bvol = bt_header.index('bool_volume')
    for data in bt_read:
        bvol = int(data[index_bvol])
        if bvol == 0:
            count0 += 1
        elif bvol == 1:
            count1 += 1
        elif bvol == 2:
            count2 += 1

with open(tally_file, 'a', newline='') as tally:
    tally_write = csv.writer(tally)
    data = [date, span, count0, count1, count2]
    tally_write.writerow(data)

sys.stdout.write('Appended data to tally.csv\n')
