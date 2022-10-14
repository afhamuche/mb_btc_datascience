#!/usr/bin/env python3

import csv
import math, copy
import numpy as np

filename = "historical_1665696314-1665005114.csv"
histogram = 'histogram_' + filename

def sigmoid(z):
    """
    Compute the sigmoid of z

    Args:
        z (ndarray): A scalar, numpy array of any size.

    Returns:
        g (ndarray): sigmoid(z), with the same shape as z

    """
    g = (1+np.exp(-z))**-1
    return g

def compute_cost(X, y, w, b, lambda_= 1):
    """
    Computes the cost over all examples
    Args:
      X : (ndarray Shape (m,n)) data, m examples by n features
      y : (array_like Shape (m,)) target value
      w : (array_like Shape (n,)) Values of parameters of the model
      b : scalar Values of bias parameter of the model
      lambda_: unused placeholder
    Returns:
      total_cost: (scalar)         cost
    """

    m, n = X.shape
    cost = 0
    for i in range(m):
        z_i = np.dot(X[i], w) + b
        fwb_i = sigmoid(z_i)
        cost += -1*y[i]*np.log(fwb_i) - (1-y[i])*np.log(1-fwb_i)
    cost = cost / m
    total_cost = cost
    return total_cost

def compute_gradient(X, y, w, b, lambda_=None):
    """
    Computes the gradient for logistic regression

    Args:
      X : (ndarray Shape (m,n)) variable such as house size
      y : (array_like Shape (m,1)) actual value
      w : (array_like Shape (n,1)) values of parameters of the model
      b : (scalar)                 value of parameter of the model
      lambda_: unused placeholder.
    Returns
      dj_dw: (array_like Shape (n,1)) The gradient of the cost w.r.t. the parameters w.
      dj_db: (scalar)                The gradient of the cost w.r.t. the parameter b.
    """
    m, n = X.shape
    dj_dw = np.zeros(w.shape)
    dj_db = 0.
    for i in range(m):
        fwb_i = sigmoid(np.dot(X[i],w) + b)
        err_i = fwb_i - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err_i * X[i,j]
        dj_db += err_i
    dj_dw = dj_dw/m
    dj_db = dj_db/m
    return dj_db, dj_dw

def gradient_descent(X, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters, lambda_):
    """
    Performs batch gradient descent to learn theta. Updates theta by taking
    num_iters gradient steps with learning rate alpha

    Args:
      X :    (array_like Shape (m, n)
      y :    (array_like Shape (m,))
      w_in : (array_like Shape (n,))  Initial values of parameters of the model
      b_in : (scalar)                 Initial value of parameter of the model
      cost_function:                  function to compute cost
      alpha : (float)                 Learning rate
      num_iters : (int)               number of iterations to run gradient descent
      lambda_ (scalar, float)         regularization constant

    Returns:
      w : (array_like Shape (n,)) Updated values of parameters of the model after
          running gradient descent
      b : (scalar)                Updated value of parameter of the model after
          running gradient descent
    """

    # number of training examples
    m = len(X)

    # An array to store cost J and w's at each iteration primarily for graphing later
    J_history = []
    w_history = []

    for i in range(num_iters):

        # Calculate the gradient and update the parameters
        dj_db, dj_dw = gradient_function(X, y, w_in, b_in, lambda_)

        # Update Parameters using w, b, alpha and gradient
        w_in = w_in - alpha * dj_dw
        b_in = b_in - alpha * dj_db

        # Save cost J at each iteration
        if i<100000:      # prevent resource exhaustion
            cost =  cost_function(X, y, w_in, b_in, lambda_)
        # Print cost every at intervals 10 times or as many iterations if < 10
        if i% math.ceil(num_iters/10) == 0 or i == (num_iters-1):
            w_history.append(w_in)
    return w_in, b_in, J_history, w_history

def predict(X, w, b):
    """
    Predict whether the label is 0 or 1 using learned logistic
    regression parameters w

    Args:
    X : (ndarray Shape (m, n))
    w : (array_like Shape (n,))      Parameters of the model
    b : (scalar, float)              Parameter of the model

    Returns:
    p: (ndarray (m,1))
        The predictions for X using a threshold at 0.5
    """
    m, n = X.shape
    p = np.zeros(m)
    for i in range(m):
        z_wb = 0

        for j in range(n):
            zwb_ij = X[i,j] + w[j]
            z_wb += zwb_ij
        z_wb += b
        f_wb = sigmoid(z_wb)
        p[i] = f_wb >= 0.5
    return p

with open(histogram, 'r') as ifile:
    histogramobj = csv.reader(ifile)

    X_train = np.array(next(histogramobj))

    buy_X_train, buy_y_train = X_train, np.array(next(histogramobj))
    sell_X_train, sell_y_train = \
        np.array(next(histogramobj)), np.array(next(histogramobj))

X_train = np.asarray(X_train, dtype=int)
X_train[-1] = np.max(X_train)*4

y_train = np.asarray(buy_y_train, dtype=int)
sell_X_train, sell_y_train = X_train, np.asarray(sell_y_train, dtype=int)

y_train = np.array([y_train, sell_y_train])
y_train = np.transpose(y_train)

X_train, y_train = y_train, X_train

m, n = X_train.shape

initial_w = np.zeros(n)
initial_b = 0.
cost = compute_cost(X_train, y_train, initial_w, initial_b)

dj_db, dj_dw = compute_gradient(X_train, y_train, initial_w, initial_b)

np.random.seed(1)
intial_w = 0.01 * (np.random.rand(2).reshape(-1,1) - 0.5)
initial_b = -8

# Some gradient descent settings
iterations = 10000
alpha = 0.001

w,b, J_history,_ = gradient_descent(\
    X_train ,y_train, initial_w, initial_b, \
    compute_cost, compute_gradient, alpha, iterations, 0)

p = predict(X_train, w, b)
print('Train Accuracy: %f'%(np.mean(p == y_train) * 100))
