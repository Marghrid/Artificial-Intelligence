# # # # # # # # # # # # # # # #
#  Grupo 3:                   #
#    80832 Margarida Ferreira #
#    81805 Duarte David       #
# # # # # # # # # # # # # # # #

import numpy as np

def Q2pol(Q, eta=5):
    return np.exp(eta*Q)/np.dot(np.exp(eta*Q),np.array([[1,1],[1,1]])) 
    
class myRL:
    def __init__(self, nS, nA, gamma):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.Q = np.zeros((nS,nA))
    
    def traces2Q(self, trace):
        self.Q = np.zeros((self.nS,self.nA))
        nQ = np.zeros((self.nS,self.nA))
        err = 1
        initial_alpha = 0.5
        i = 0
        while err>=1e-2:
            i+=1
            alpha = (5/(5+i))*initial_alpha
            for tt in trace:
                #[x, a, y, r]
                nQ[int(tt[0]),int(tt[1])] = nQ[int(tt[0]),int(tt[1])] + alpha * (tt[3] + self.gamma * max(nQ[int(tt[2]),:]) - nQ[int(tt[0]),int(tt[1])])
            err = np.linalg.norm(self.Q-nQ)
            self.Q = np.copy(nQ)
        #Number of iterations:
        #print(i)
        return self.Q
