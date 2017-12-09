from sklearn.externals import joblib
lista = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
outralista = []

#for coisa in joblib.load('traj1.pkl'):
#    print(coisa)

#for coisa in joblib.load('traj1.pkl'):
#    lista[int(coisa[0])][int(coisa[2])] = int( coisa[1]+1)
#
#for l in lista:
#    for c in l:
#        print(c, end=' ')
#    print();

#count_bons = count_maus = 0;
#
#for coisa in joblib.load('traj1.pkl'):
#    temp_list = []
#    for coisinha in coisa:
#        temp_list += [(int(coisinha))]
#
#    if temp_list not in outralista:
#        outralista += [temp_list]
#
#    if temp_list == [5, 0, 5, 0]:
#        count_maus += 1
#    elif temp_list == [5, 0, 6, 0]:
#        count_bons += 1
#
#for i in outralista:
#    print (i)
#
#print("para 5")
#print(count_maus)
#print("para 6")
#print(count_bons)

print("TRAJ 1:")
for coisa in joblib.load('traj1.pkl'):
    temp_list = []
    for coisinha in coisa:
        temp_list += [(int(coisinha))]
    if temp_list not in outralista:
        outralista += [temp_list]

for i in outralista:
    print (i)

outralista = []

print("TRAJ 2:")
for coisa in joblib.load('traj2.pkl'):
    temp_list = []
    for coisinha in coisa:
        temp_list += [(int(coisinha))]
    if temp_list not in outralista:
        outralista += [temp_list]
for i in outralista:
    print (i)
