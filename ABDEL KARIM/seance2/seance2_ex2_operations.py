import numpy as np
l = list(range(10))
print("Liste de base : ",l)
t = np.array(l)
print("Liste numpy : ",t)
print("Avec numpy on ajoute 2 : ",t+2) # avec numpy, on peut faire des opérations mathématiques directement avec la liste

valeursCOS = np.cos(np.radians(t))
print(valeursCOS)

tableau=np.linspace(0.1, 1.0, 10)
print(tableau*2)

AD = np.array(range(5))
BD = np.array(range(5,10))
print(AD)
print(BD)
print(AD*BD)

AM = np.array([
    [1,2],[3,4]
])

BM = np.array([
    [5,6],[7,8]
])

print("Matrice A : ",AM)
print("Matrice B : ",BM)
print("Résultat : ",AM*BM)
print("Multiplication matricielle : ",AM@BM)