import numpy as np

v0 = 450
alpha = np.radians(45)
g = 9.81
m = 18
dt = 0.1
k = 0.3

v0x = v0 * np.cos(alpha)
v0z = v0 * np.sin(alpha)

positions = np.array([[0.00] ,[0.00]])
vitesse = np.array([[v0x] ,[v0z]])


a0x = -( k /m ) * v0x
a0z = - g -( k /m ) * v0z

acceleration = np.array([[a0x] ,[a0z]])

while  positions[1,-1] >= 0 :

    ax = -( k /m ) * vitesse[0 ,-1]
    az = - g -( k /m ) * vitesse[1 ,-1]
    acceleration = np.append(acceleration, [[ax] ,[az]], axis = 1)

    vx = vitesse[0 ,-1] + ax * dt
    vz = vitesse[1 ,-1] + az * dt
    vitesse = np.append(vitesse, [[vx] ,[vz]], axis = 1)

    x = positions[0 ,-1] + vx * dt
    z = positions[1 ,-1] + vz * dt
    positions = np.append(positions, [[x] ,[z]], axis = 1)

impact = positions[0 ,-1]
print("L'impact : ",impact)

max_indice = np.argmax(positions[1 ,:])
x_maxHauteur = positions[0 ,max_indice]

print(x_maxHauteur)