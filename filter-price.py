#!/usr/bin/env python3

import csv
import pandas
import numpy

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

def get_bool(aType):
    return aType == 'buy'

def get_intervals(maximum, average, minimum, interval):
    aList = []
    intervals = (int(maximum - minimum) // interval) + 2

    for i in range(intervals):
        aList.append(int((i*interval) - average + minimum))
    return aList

filename = "historical_1665783247-1665178447.csv"
pricesfile = "price_" + filename

with open(pricesfile, 'w', newline='') as prices:
    pricesobj = csv.writer(prices)
    bool_header = ['type', 'price', 'volume']
    pricesobj.writerow(bool_header)

    with open(filename,'r', newline='') as historical:
        historicalobj = csv.reader(historical)
        header = next(historicalobj)

        for data in historicalobj:
            aList = []
            aList.append(get_bool(data[4]))
            aList.append(float(data[2]))
            aList.append(float(data[6]))
            pricesobj.writerow(aList)


dataset = pandas.read_csv(pricesfile, header=0)

buy = dataset.iloc[:, 0].values
buy = numpy.asarray(buy, dtype=bool)
price = dataset.iloc[:, 1].values
price = numpy.asarray(price, dtype=float)
average = numpy.average(price)
minimum = numpy.min(price)
volume = dataset.iloc[:, 2].values
volume = numpy.asarray(volume, dtype=float)

intervals = get_intervals(numpy.max(price), average, minimum, 25)
bool_header += intervals

with open(pricesfile, 'w', newline='') as prices:
    pricesobj = csv.writer(prices)
    pricesobj.writerow(bool_header)

    length = len(price)

    for i in range(length):
        aList = []
        aprice = price[i]
        aList.append(buy[i])
        aList.append(aprice)
        aList.append(volume[i])
        aList += bool_list(int(aprice - average), intervals)
        pricesobj.writerow(aList)
