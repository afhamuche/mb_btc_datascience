#!/usr/bin/env python3
import requests
import json
import datetime
import csv
import sys

def gettrades(time0, time1):
    trades = requests.get(trades_url + '/' + str(time0) + '/' + str(time1))
    trades = json.loads(trades.text)
    return trades

def timebackdays(timestamp, days):
    return int(timestamp - (3600 * 24 * days))

def getsatoshi(afloat):
    return int(afloat * 100000000)

def getvolume(amount, price):
    return amount*price

coin = 'BTC'
mb_api = 'https://www.mercadobitcoin.net/api/'
trades_url = mb_api + coin + '/trades'
date_now = datetime.datetime.now()
timestamp = int(date_now.timestamp())

args = len(sys.argv)

if args == 3:
    days = int(sys.argv[1])
    interval = int(sys.argv[2])
else:
    days = int(input("Enter days back to fetch: ")) #10
    interval = int(input("Enter interval (seconds [def. 500]): ")) #500 seconds

time = timebackdays(timestamp, days)
filename = 'trades-' + date_now.strftime("%Y%m%d") + '-' + str(days) + '.csv'

keys = ['amount', 'date', 'price', 'tid', 'type', 'satoshi', 'volume']
db_insert = []

with open("./csv_files/" + filename, 'w', newline='') as historical:

    writer = csv.writer(historical)
    writer.writerow(keys)

    while time < timestamp:
        trades = gettrades(time, time + interval)
        for trade in trades:
            db_insert = list(trade.values())
            amount = float(db_insert[0])
            price = float(db_insert[2])
            db_insert.append(getsatoshi(amount))
            db_insert.append(getvolume(amount, price))
            writer.writerow(db_insert)
        time += interval + 1

sys.stdout.write(filename + '\n')
