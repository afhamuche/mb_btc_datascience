#!/usr/bin/env python3

import csv
import sys

args = len(sys.argv)
if args>1:
    filename = sys.argv[1]
else:
    filename = "historical_1665783247-1665178447.csv"
sys.stdout.write(filename + '\n')

pricefile = "price_" + filename
sys.stdout.write(pricefile + '\n')

histogramfile = 'histogram_' + pricefile

for x in range(2):
    if x==0:
        awtype = 'w'
    else:
        awtype = 'a'

    with open(histogramfile, awtype, newline='') as histogram:
        histogramobj = csv.writer(histogram)

        with open(pricefile, 'r', newline='') as readfile:
            readobj = csv.reader(readfile)
            header = next(readobj)
            header = header[3:]
            header_max = header[-1]
            header_size = len(header)
            histogramobj.writerow(header)

            aList = []
            for i in range(header_size):
                aList.append(0)

            for row in readobj:
                aBool = row[0] == "True"
                tmpList = row[3:]
                if aBool and awtype == 'w':
                    placement = tmpList.index('True')
                    aList[placement] += 1
                elif awtype == 'a' and not aBool:
                    placement = tmpList.index('True')
                    aList[placement] += 1

            histogramobj.writerow(aList)
sys.stdout.write(histogramfile + '\n')
