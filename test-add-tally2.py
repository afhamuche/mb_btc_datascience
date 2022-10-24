#!/usr/bin/env python3
import csv
import sys
import re
import pandas

def btype_col(btype, bool_bias):
    if btype:
        return bool_bias + 1
    else:
        return bool_bias - 1

def bvol_cols(bvol, c0, c1, c2):
    if bvol == 0:
        return c0 + 1, c1, c2
    elif bvol == 1:
        return c0, c1 + 1, c2
    elif bvol == 2:
        return c0, c1, c2 + 1

args = len(sys.argv)
if args>1:
    filename = str(sys.argv[1])
else:
    filename = str(input("Filename for trades dataset: "))

bt_file = 'bigtable_' + filename
csv_path = "./csv_files/"
bt_path = csv_path + "bigtable_trades/"
tally_file = "tally2.csv"

#['date', 'span', 'bool_bias', 'mean_price', 'mean_price_var', 'mean_vol', 'vol_0', 'vol_1', 'vol_2']

x = re.search(r"[0-9]{8}-[0-9]*", filename)
date = x[0][0:8]
span = re.search(r"[0-9]*$", x[0])
span = span[0]
c0, c1, c2 = 0, 0, 0

df = pandas.read_csv(bt_path + bt_file)
mean_price = df['price'].mean()
mean_vol = df['volume'].mean()
mean_price_var = df['var_mean'].mean()
bool_bias = 0

with open(bt_path + bt_file, 'r', newline='') as bigtable:
    bt_read = csv.reader(bigtable)
    bt_header = next(bt_read)
    index_bvol = bt_header.index('bool_volume')
    index_btype = bt_header.index('bool_type')
    for data in bt_read:
        bvol = int(data[index_bvol])
        btype = bool(data[index_btype])
        bool_bias = btype_col(btype, bool_bias)
        c0, c1, c2 = bvol_cols(bvol, c0, c1, c2)

mean_price = '{:.2f}'.format(mean_price)
mean_price_var = '{:.3f}'.format(mean_price_var)
mean_vol = '{:.2f}'.format(mean_vol)

with open(tally_file, 'a', newline='') as tally:
    tally_write = csv.writer(tally)
    '''
    header = \
        ['date', 'span', 'bool_bias', 'mean_price', 'mean_price_var', 'mean_vol', 'vol_0', 'vol_1', 'vol_2']
    tally_write.writerow(header)
    '''
    data = \
        [date, span, bool_bias, mean_price, mean_price_var, mean_vol , c0, c1, c2]
    tally_write.writerow(data)

sys.stdout.write('Appended data to tally.csv\n')
