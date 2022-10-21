#!/usr/bin/env python3

import csv
import sys
import pandas

args = len(sys.argv)
if args>1:
    filename = str(sys.argv[1])
else:
    filename = str(input("Filename for historical dataset: "))

ifile = "new_" + filename

aheader = ['timestamp', 'tid', 'bool_type', 'satoshi', 'price', 'volume', 'var_mean', 'bool_volume']

df = pandas.read_csv(filename)
average = df['price'].mean()

with open(filename,'r', newline='') as historical:
    historical_read = csv.reader(historical)
    header = next(historical_read)

    index_timestamp = header.index('date')
    index_tid = header.index('tid')
    index_type = header.index('type')
    index_satoshi = header.index('satoshi')
    index_price = header.index('price')
    index_volume = header.index('volume')

    with open(ifile, 'w', newline='') as ifile:
        ifile_write = csv.writer(ifile)
        ifile_write.writerow(aheader)

        for data in historical_read:
            alist = []
            alist.append(data[index_timestamp])
            alist.append(data[index_tid])
            if data[index_type] == 'buy':
                alist.append(True)
            else:
                alist.append(False)
            alist.append(data[index_satoshi])

            price = float(data[index_price])
            price = float('{:.3f}'.format(price))

            alist.append(price)

            volume = '{:.2f}'.format(float(data[index_volume]))
            volume = float(volume)

            alist.append(volume)

            var_mean = price - average
            var_mean = var_mean / average
            var_mean = float('{:.3}'.format(var_mean))

            alist.append(var_mean)

            if volume < 100:
                volume = 0
            elif volume > 20000:
                volume = 1
            else:
                volume = 2

            alist.append(volume)
            ifile_write.writerow(alist)

sys.stdout.write(str(ifile) + '\n')
