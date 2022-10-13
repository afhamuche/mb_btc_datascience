#!/usr/bin/env python3

import csv
filename = "historical_1665696314-1665005114.csv"

def bool_list(amount, cols):
    length = len(cols)
    aList = []

    for i in range(length):
        if amount < cols[i]:
            aList.append(True)
            for j in range(length - len(aList)):
                aList.append(False)
            break
        else:
            aList.append(False)
    if not(True in aList):
        aList[-1] = True
    return aList

def get_intervals(maximum, interval):
    intervals = []
    for i in range(maximum//interval):
        intervals.append(interval*(i+1))
    intervals.append(0)
    return intervals


for j in range(2):
    with open(filename,'r', newline='') as historical:
        header = next(csv.reader(historical))
        bool_header = ['tid', 'volume']
        intervals = get_intervals(10000, 100)
        bool_header += intervals

        if j == 0:
            filter_split = 'buy'
        else:
            filter_split = 'sell'

        fsfile = filter_split + "_" + filename
        fswriter = open(fsfile, 'w', newline='')
        obj = csv.writer(fswriter)
        obj.writerow(bool_header)
        for data in csv.reader(historical):
            obj_list = []
            if data[4] == filter_split:
                obj_list.append(data[3])
                obj_list.append(data[6])
                obj_list.extend(bool_list(float(data[6]), bool_header[2:]))
                obj.writerow(obj_list)

        fswriter.close()
