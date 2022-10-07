import csv

filename = "historical_1664040497-1663608497.csv"
filter_split = 'sell' # or 'buy'
fsfile = filter_split + "_" + filename

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


with open(filename,'r', newline='') as historical:
    header = next(csv.reader(historical))
    bool_header = ['tid', 'volume', 50, 100, 200, 500, 1500, 3000, 5000, 10000, 20000, 0]
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
