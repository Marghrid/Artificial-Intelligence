import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

def vowel_ratio(X):
    vowels = 0
    for l in X:
        if l == 'A' or l == 'E' or l ==  'I' or l == 'O' or l == 'U'\
           or l == 'a' or l == 'e' or l ==  'i' or l == 'o' or l == 'u':
            vowels += 1
    return vowels/len(X)

def numbers_ratio(X):
    numbers = 0
    for l in X:
        if l >= '0' and l >= '9':
            numbers += 1
    return numbers/len(X)

def features(X):
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = ord(X[x][0])
        F[x,2] = ord(X[x][1])
        F[x,3] = ord(X[x][-1])
        F[x,4] = vowel_ratio(X)
    return F     

def mytraining(f,Y):
    
    #KNeighborsClassifier
    n_neighbors = 3
    weights = 'distance'
    clfKNNC2 = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf = clfKNNC2.fit(f, Y)    
   
    return clf
    
def mytrainingaux(f,Y,par):
    
    return clf

def myprediction(f, clf):
    Ypred = clf.predict(f)
    return Ypred

