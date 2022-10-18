#!/usr/bin/env python3

import csv
import sys

args = len(sys.argv)
if args>1:
    filename = sys.argv[1]
else:
    filename = "historical_1665783247-1665178447.csv"

histogram = 'histogram_' + filename

def compute_cost(x, y, w, b):

    m = len(x)
    cost = 0

    for i in range(m):
        f_wb = w * x[i] + b
        cost = cost + (f_wb - y[i])**2
    total_cost = 1 / (2 * m) * cost

    return total_cost

def compute_gradient(x, y, w, b):
    m = len(x)
    dj_dw = 0
    dj_db = 0

    for i in range(m):
        f_wb = w * x[i] + b
        dj_dw_i = (f_wb - y[i]) * x[i]
        dj_db_i = f_wb - y[i]
        dj_db += dj_db_i
        dj_dw += dj_dw_i
    dj_dw = dj_dw / m
    dj_db = dj_db / m

    return dj_dw, dj_db

def gradient_descent(x, y, w_in, b_in, alpha, num_iters):
    b = b_in
    w = w_in

    for i in range(num_iters):
        #print("Iter[{i}]: w= {w} & b= {b}")
        dj_dw, dj_db = compute_gradient(x, y, w , b)
        b = b - alpha * dj_db
        w = w - alpha * dj_dw
        print("Iter[{}]: w= {} & b= {}".format(i, w, b))

    return w, b


sys.stdout.write(histogram + '\n')
with open(histogram, 'r') as ifile:
    histogramobj = csv.reader(ifile)

    '''
    # Load our data set
    buy_x_train = np.array(next(histogramobj))   #features
    buy_y_train = np.array(next(histogramobj))   #target value
    sell_x_train = np.array(next(histogramobj))
    sell_y_train = np.array(next(histogramobj))

    buy_x_train = np.asarray(buy_x_train, dtype=float)
    buy_y_train = np.asarray(buy_y_train, dtype=int)
    buy_x_train[-1] = 1000000
    sell_y_train = np.asarray(sell_y_train, dtype=int)
    sell_x_train = np.asarray(sell_x_train, dtype=float)
    sell_x_train[-1] = 1000000
    '''

    buy_x_train = next(histogramobj)
    buy_y_train = next(histogramobj)
    sell_x_train = next(histogramobj)
    sell_y_train = next(histogramobj)

    for i in range(len(buy_x_train)):
        buy_x_train[i] = int(buy_x_train[i])
        buy_y_train[i] = int(buy_y_train[i])
        sell_x_train[i] = int(sell_x_train[i])
        sell_y_train[i] = int(sell_y_train[i])
    buy_x_train[-1] = 58000

    for i in range(3):
        if i <1:
            print("buy (x) vs sell (y)")
            x_train = buy_y_train
            y_train = sell_y_train
            in_usr = input()
        elif i<2:
            print("bool (x) vs buy (y)")
            x_train = buy_x_train
            y_train = buy_y_train
            in_usr = input()
        else:
            print("bool (x) vs sell (y)")
            x_train = buy_x_train
            y_train = sell_y_train
            in_usr = input()
        # initialize parameters
        w_init = 0
        b_init = 0
        # some gradient descent settings
        iterations = 8
        tmp_alpha = 1.0e-0
        # run gradient descent
        w_final, b_final = \
            gradient_descent(x_train, y_train, w_init, b_init, \
            tmp_alpha, iterations)# compute_cost, compute_gradient)
        print("w_final = " + str(w_final))
        print("b_final = " + str(b_final))
        print(f"(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})")
