#!/usr/bin/env python3

import csv
import sys

args = len(sys.argv)
if args>1:
    filename = sys.argv[1]
else:
    filename = "historical_1665783247-1665178447.csv"

histogramfile = 'histogram_' + filename

with open(histogramfile, 'w') as histogram:
    histogramobj = csv.writer(histogram)

    ifile = 'buy_' + filename
    for j in range(2):
        with open(ifile,'r', newline='') as readfile:
            readobj = csv.reader(readfile)
            header = next(readobj)
            header = header[2:]
            header_max = header[-2]
            histogramobj.writerow(header)
            aList = []
            for i in range(len(header)):
                aList.append(0)

            for row in readobj:
                placement = row.index('True') - 2
                aList[placement] += 1

            histogramobj.writerow(aList)
        sys.stdout.write(ifile + '\n')
        ifile = 'sell_' + filename
sys.stdout.write(histogramfile + '\n')
