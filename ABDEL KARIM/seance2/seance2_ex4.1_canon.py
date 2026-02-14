import numpy as np

v0=450
alpha = np.radians(45)
g = 9.81
m=18
dt = 1

# composante v0
v0x = v0*np.cos(alpha)
v0z = v0*np.sin(alpha)

vitesse = np.array([
    [v0x],[v0z]
])

positions = np.array([
    [0],[0]
])

temps = np.arange(0,60,dt)

compteur = 0

while compteur < len(temps) and positions[1, -1] >= 0:
    t = temps[compteur]
    x = v0x * t
    z = -0.5 * g * t ** 2 + v0z * t

    positions = np.append(positions, [[x],[z]], axis=1)
    compteur += 1

print(positions)
impactX = positions[0, -1]
indice_max = np.argmax(positions[1, :])
hauteur_max = positions[0, indice_max]
print("hauteur maximal : ", hauteur_max)