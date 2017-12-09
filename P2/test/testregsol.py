import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import timeit
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import regsol

tres = [.2, 100]    
for ii, test in enumerate(["regress.npy", "regress2.npy"]):
	for alpha in (0.00001, 0.0001, 0.001, 0.01, 0.1, 0.2):
		for gamma in (0.001, 0.005, 0.01, 0.05, 0.1, 0.12, 0.15, 0.2, 0.3):
			X,Y,Xp,Yp = np.load(test)
			
			reg = regsol.mytrainingaux(X,Y, (alpha, gamma))
			
			Ypred = regsol.myprediction(Xp,reg)
			
			# Teste de score:
			
			#if -cross_val_score( reg, X, Y, cv = 5, scoring = 'neg_mean_squared_error').mean() < tres[ii]:
			print("Testing ridge ", test, ", with alpha = ", alpha, " and gamma = ", gamma)
			print("Score:", end = ' ')
			print(-cross_val_score( reg, X, Y, cv = 5, scoring = 'neg_mean_squared_error').mean())
			print("")
