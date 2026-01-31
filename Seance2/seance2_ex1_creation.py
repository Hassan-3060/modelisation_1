# Section import
from importlib.metadata import requires
from tkinter.filedialog import Open

import numpy as np
from numpy.ma.core import append

#2.1.2
## Exercice 1.2

a = np.array(np.arange(1,7))

b = np.array([
    [range(1,4)],
    [range(4,7)]
])

c = np.array([
    [
        [111, 112], [121, 122]
    ],
    [
        [211, 212], [221, 222]
    ]
])
## Exercice 1.3
tableau_linspace = np.linspace(0,1,10)
tableau_arange = np.arange(0,1,0.1)

#tableau_range = range(0,1,0.1) float n'est pas pris en compte dans range
# Alors l'intérêt de linspace et arange c'est qu'ils supportent les float et peuvent aussi faire des calculs en utilisant des fonctions mathématiques