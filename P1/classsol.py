import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

vowels = ['a', 'e', 'i', 'o', 'u']

# As funções number_of_values, first_letter_vowel last_letter_vowel foram
#  usadas para testar diferentes features para o classificador.

def number_of_vowels(X):
    """ Returns the number of vowels in the word X """
    n_vowels = 0
    for l in X:
        if l in vowels:
            n_vowels += 1
    return n_vowels

def first_letter_vowel(X):
    """ Returns 1 if the first letter of the word is a vowel and 0 if it isn't """
    return int(X[0] in vowels)

def last_letter_vowel(X):
    """ Returns 1 if the last letter of the word is a vowel and 0 if it isn't """
    return int(X[-1] in vowels)

def features(X):
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = len(X[x])
        F[x,1] = ord(X[x][0])  #Primeira letra da palavra
        F[x,2] = ord(X[x][1])  #Segunda letra da palavra
        F[x,3] = ord(X[x][-2]) #Penúltima letra da palavra
        F[x,4] = ord(X[x][-1]) #Última letra da palavra
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
