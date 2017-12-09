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
for ii, test in enumerate(["regress2.npy"]):
	X,Y,Xp,Yp = np.load(test)
	
	reg = regsol.mytrainingaux(X,Y, (0.0001, 0.01))
	
	Ypred = regsol.myprediction(Xp,reg)
	
	# Teste de score:
	
	if -cross_val_score( reg, X, Y, cv = 5, scoring = 'neg_mean_squared_error').mean() < tres[ii]:
		print("Testing ridge ", test)
		print("Erro dentro dos limites de tolerância. OK")
		print("Score:", end = ' ')
		print(-cross_val_score( reg, X, Y, cv = 5, scoring = 'neg_mean_squared_error').mean())
		print("")

	plt.figure()
	plt.plot(Xp,Yp,'g.',label='datatesting')
	plt.plot(X,Y,'k+',label='datatrain')
	plt.plot(Xp,Ypred,'m',label='linregres2')
	plt.legend( loc = 1 )
	
	#NOSSO:
	plt.show()