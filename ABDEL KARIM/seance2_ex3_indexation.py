import numpy as np
tableau=np.arange(1,10,2)
print(tableau)
print(tableau[0])
print(tableau[1])
print(tableau[-1])

tableau2D=np.array([
    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
])
print(tableau2D)

tableau2D=np.reshape(tableau2D,(4,4))
print(tableau2D)

element=tableau2D[:,-1]
print(element)

elements2D = tableau2D[0:2, 0:2]
print(elements2D)

tableau2D[3,:] = 99
print(tableau2D)

