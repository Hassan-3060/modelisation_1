import numpy as np

v0=450
alpha = np.radians(45)
g = 9.81
m=18
dt = 1

# composante v0
v0x = v0*np.cos(alpha)
v0y = v0*np.sin(alpha)

vitesse = np.array([
    [v0x],[v0y]
])

positions = np.array([
    [0],[0]
])

temps = np.arange(0,60,dt)
print(temps)

