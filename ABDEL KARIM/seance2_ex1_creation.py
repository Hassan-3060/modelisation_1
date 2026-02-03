import numpy as np

liste = [1,2,3,4,5,6,7,8,9,10]
print(liste)

a = np.array(liste)
print(a)

b = np.array([
    [1, 2, 3], [4, 5, 6]
])
print(b)

n=np.array([
    [
        [111, 112],[121,122]
    ],
    [
        [211,212],[221,222]
    ]
])

tableau_space = np.linspace(0, 1, 10)

tableau_arange = np.arange(0, 1, 0.1)

#tableau_range = range(0, 1, 10) erreur, la fonction range ne prend pas en compte les float

