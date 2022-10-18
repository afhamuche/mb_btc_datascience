#!/usr/bin/env python3

import csv
import sys

args = len(sys.argv)
if args>1:
    filename = sys.argv[1]
else:
    filename = input("filename.csv = ")

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
        total_cost = compute_cost(x, y, w, b)
        print("Total cost: {}".format(total_cost))

    return w, b


sys.stdout.write(histogram + '\n')
with open(histogram, 'r') as ifile:
    histogramobj = csv.reader(ifile)

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
        elif i<2:
            print("bool (x) vs buy (y)")
            x_train = buy_x_train
            y_train = buy_y_train
        else:
            print("bool (x) vs sell (y)")
            x_train = buy_x_train
            y_train = sell_y_train

        w_init = 0
        b_init = 0
        # some gradient descent settings
        #iterations = 10000
        #tmp_alpha = 1.0e-8
        iterations = int(input("iterations: "))
        tmp_alpha = float(input("alpha: "))

        w_final, b_final = \
            gradient_descent(x_train, y_train, w_init, b_init, \
            tmp_alpha, iterations)# compute_cost, compute_gradient)
        print("w_final = " + str(w_final))
        print("b_final = " + str(b_final))
        print(f"(w,b) found by gradient descent: ({w_final:.4f},{b_final:.4f})")
