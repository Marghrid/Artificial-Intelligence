from sklearn.externals import joblib
lista = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
outralista = []

for coisa in joblib.load('traj1.pkl'):
    print(coisa)

for coisa in joblib.load('traj1.pkl'):
    lista[int(coisa[0])][int(coisa[2])] = int( coisa[1]+1)

for l in lista:
    for c in l:
        print(c, end=' ')
    print();

cout_bons = cout_maus = 0;

for coisa in joblib.load('traj1.pkl'):
    temp_list = []
    for coisinha in coisa:
        temp_list += [(int(coisinha))]

    if temp_list not in outralista:
        outralista += [temp_list]

    if temp_list == [5, 0, 5, 0]:
        cout_maus += 1
    elif temp_list == [5, 0, 6, 0]:
        cout_bons += 1

for i in outralista:
    print (i)

print("para 5")
print(cout_maus)
print("para 6")
print(cout_bons)
