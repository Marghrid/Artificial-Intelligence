# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""
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
        alpha = 0.1
        while err>=1e-2:
            for tt in trace:
                #[x, a, y, r]
                nQ[int(tt[0]),int(tt[1])] = nQ[int(tt[0]),int(tt[1])] + alpha * (tt[3] + self.gamma * max(nQ[int(tt[2]),:]) - nQ[int(tt[0]),int(tt[1])])
            err = np.linalg.norm(self.Q-nQ)
            self.Q = np.copy(nQ)
    
        return self.Q
