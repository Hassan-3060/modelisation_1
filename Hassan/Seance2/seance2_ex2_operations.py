# section import
from random import *
import numpy as np
from numpy.ma.core import shape

# Exercice 2.1
#l = list(range(10))
#t = np.array(l)
#print(t+2) # l+2 ne fonctionne pas car on peut pas concaténer un entier avec une liste, alors t+2 ajoutera 2 à chaque nombre dans la liste t
#print(np.cos(t))
#tableau = np.linspace(0.1,1, 10)
#tableau *= 2
#print(tableau)

# Exercice 2.2
tableau1 = np.array(range(1,6))
tableau2 = np.array(range(1,6))
tableau1 *= 2
tableau2 *= 2

A = np.array([
    [1,2],[3,4]
])

B = np.array([
    [5,6],[7,8]
])

D = np.dot(A,B)
print(D)

D = A@B
print(D)