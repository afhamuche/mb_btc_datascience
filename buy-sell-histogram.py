#!/usr/bin/env python3

import csv

filename = "historical_1665696314-1665005114.csv"
intervals = 100

with open('histogram_' + filename, 'w') as histogram:
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
        ifile = 'sell_' + filename
