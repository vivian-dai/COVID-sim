import numpy as np
from scipy.special import logsumexp
from random import uniform

def train_log_regression(factors, covid_status, learning_rate, max_iter):
    """ Inputs: train_factors, train_covid_status, learning rate,
        and max num of iterations in gradient descent
        the covid status should be a N*1 binary matrix, represent whether the person is infected
        Returns the trained weights (w/o intercept)"""
    N_data, D_data = factors.shape
    K_data = covid_status.shape[1]
    weights = np.zeros((D_data, K_data))

    y = np.zeros(shape=(N_data, K_data))
    for iter in range(max_iter):
        for n in range(N_data):
            for k in range(K_data):
                y[n][k] = np.exp(np.dot(factors[n],weights[:,k]))/sum(np.exp(np.dot(covid_status[n],weights)))
        gradient = np.matmul(np.transpose(factors),y-covid_status)
        weights = weights - learning_rate*gradient

    w0 = None
    return weights, w0

def log_softmax(factors, weights, w0=None):
    """ Inputs: factors, and weights, should be different factors from the dataset used by training
        Returns the log_softmax values."""
    if w0 is None: w0 = np.zeros(weights.shape[1])
    # a N*K matrix is supposed to be returned
    N_data = factors.shape[0]
    K_data = weights.shape[1]
    # append w0 to weights
    weights = np.concatenate(([w0], weights), axis=0)
    # append a column of 1 to factor matrix to accommdate w0
    x0 = np.full((N_data, 1), 1)
    images = np.concatenate((x0, factors), axis=1)
    result = np.zeros(shape=(N_data,K_data))

    for n in range(N_data):
        for k in range(K_data):
            result[n][k] = np.dot(images[n],weights[:,k])-logsumexp(np.dot(images[n],weights))

    return result

def predict(log_softmax):
    """ Inputs: matrix of log softmax values
        Returns the predictions"""
    today = uniform(0,1)
    log_softmax = log_softmax.T
    log_softmax = log_softmax-today
    for i in range(len(log_softmax)):
        if log_softmax[i]>0:
            log_softmax[i]=1
        else:
            log_softmax[i]=0
    return log_softmax