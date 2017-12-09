import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
    # Kernel Ridge Regression
    return mytrainingaux(X, Y, (0.001, 0.1))
    
def mytrainingaux(X,Y,par):
    alpha = par[0]
    gamma = par[1]
    regkr = KernelRidge(kernel='rbf', gamma=gamma, alpha=alpha)
    reg = regkr.fit(X,Y) 
    return reg
    reg.fit(X,Y)
    return reg

def myprediction(X,reg):

    Ypred = reg.predict(X)

    return Ypred
