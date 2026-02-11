# import
import numpy as np

# Exercice 3.1
A = np.arange(1,10,2)
# En Python, l'indexation commence à 0 et terminer à n-1, n est la taille d'une liste. Alors pour afficher le premier élément d'une liste, il faut afficher avec l'indexe 0.

B = np.arange(0,16,1)
print(B)

B = np.reshape(B, (4, 4))
print(B)
B_E1 =B[0,0] # Donne 0
B_E2= B[1]
B_EAvantDernier = B[-2] # ou 2 au lieu de -2 (mais -2 est mieux pour afficher l'avant dernière ligne).
SousTableau = B[0:2, 0:2]
print(SousTableau)

B_modifier = B
B_modifier[-1] = 99
print(B_modifier)