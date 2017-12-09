import numpy as np
from sklearn.externals import joblib
from RL import *
import RLsol

print("Testing different values of gamma and alpha for Q learning with constant alpha")
print("(Printing all resuls)")
print("")

for test in [('fmdp1.pkl','traj1.pkl'), ('fmdp2.pkl','traj2.pkl')]:
    for alpha in (.1, .2, .3, .4, .5, .6, .7, .8, .9, .99, 1):
        for gamma in (.99, .9, .85,):
            #print("Testing ", test[0], " with alpha = ", alpha, " with gamma = ", gamma)    
           
            # funcoes auxiliarres
            fmdp = joblib.load(test[0]) 

            # ficheiro com a trajectória de treino             
            traj = joblib.load(test[1]) 
            
            qlearn = RLsol.myRL(7,2, alpha, gamma)

            Q, i = qlearn.traces2Q(traj)
            
            #print("Valores Q aprendidos")
            #print(qlearn.Q)
            #if np.linalg.norm(Q-fmdp.Q)<.3:
            #    print("Erro nos Q dentro dos limites de tolerância. OK")
            #else:
            #    print("Erro nos Q acima dos limites de tolerância. FAILED")
            #
            # gerar trajectoria aprendida
            J,trajlearn = fmdp.runPolicy(4,3,RLsol.Q2pol(Q))
            
            #print("Trajectoria gerada com a politica aprendida")
            #print(trajlearn)
            #if J>.7:
            #    print("Recompensa obtida dentro do previsto. OK")
            #else:
            #    print("Recompensa obtida abaixo do previsto. FAILED")

            if np.linalg.norm(Q-fmdp.Q)<.3 and J>.7:
                print("Testing", test[0], "with alpha =", alpha, "with gamma =", gamma)
                print("Iterações:", i)
                print("Recompensa:", J)
                print("Erro:", np.linalg.norm(Q-fmdp.Q))
                #print("OK")
                print("")
    
    print("")
