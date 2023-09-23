import numpy as np

def Matrix(n):
    #nc=int((1+(n-1))*(n-1)/2)
    m=np.eye(n)
    for i in range(n):
        for j in range(n):
                if(j>i):
                   m[i][j]=float(input("enter la valeur de l'evaluation entre les deux risques :"))
                if(j<i):
                   m[i][j] =1/m[j][i]
    return m
# Calcul de vecteur de priorité
def vectPriority(M):
    n=len(M)
    # Effectuer les sommes de chaque colonne
    v1=np.sum(M,axis=0)
    M1=np.zeros((n,n))
    #Diviser chaque élément de la matrice par le total de la colonne
    for i in range(n):
        M1[i, :]=M[i, :]/v1
    vp=np.sum(M1,axis=1)/n

    #Calcul de la valeur propre max
    M2=M* vp
    v2=np.sum(M2,axis=1)/vp
    Lambda =np.average(v2)

    #Déterminer la valeur d’Indice Aléatoire (IA)
    IAs=[0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49,1.51,1.48,1.56,1.57,1.59]
    IA=IAs[n-1]

    #Calcul de l’Indice de Cohérence : IC
    IC=(Lambda-n)/(n-1)


    #Calcul de Ratio de Cohérence (RC)
    RC=IC/IA
    print("le vecteur de priorite :",*vp)
    print("\nl'indice aleatoire :",IA)
    print("\nl'indice aleatoire :",IC)
    print("\nle ration de coherence :",RC)
    return vp,RC
def AHP():
    print("******** les criteres *********")
    n=int(input("donner le nombre des criteres"))
    M=Matrix(n)
    vpc,RC=vectPriority(M)
    if(RC>0.1):
        print("le degré de cohérence de comparaison n'est pas acceptable pour le sous critere de critere ", i+1)
        exit()
    #Agrégation de Projet
    print("******** les sous criteres *********")
    vps=[]
    for i in range(n):
        print("donner le nombre des sous criteres de critere ",i+1)
        n1 = int(input())
        M1 = Matrix(n1)
        vpsi,RCs=vectPriority(M1)
        vps=np.concatenate((vps,(vpsi*vpc[i])))
        if(RCs>0.1):
            print("le degré de cohérence de comparaison n'est pas acceptable pour le sous critere de critere ",i+1)
            exit(0)

    #pour les alternatives
    print("******** les alternatives *********")
    n2 = int(input("donner le nombre des alternatives"))
    M2 = Matrix(n2)
    vpa, RCa = vectPriority(M2)
    if (RCa > 0.1):
        print("le degré de cohérence de comparaison n'est pas acceptable pour les alternatives")
        exit()
    #calcule de l'agrigation finale
    m = np.ones((n2, len(vps)))
    m=((m.T) * vpa).T
    m=m*vps


    print(m)
    print(*vps)

    #comparaison entre les alternatives
    max_index = np.argmax(m)
    max_row, max_col = np.unravel_index(max_index, m.shape)
    print("l’alternative ", max_row + 1, " se révèle être le meilleur choix")
    return