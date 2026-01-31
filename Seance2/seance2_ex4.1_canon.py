# Import
import numpy as np

# Initialisation
v0 = 450
alpha = 45
alphaRadians = np.radians(alpha)
g = 9.81
dt = 0.1

# Composantes de v0x et v0z de la vitesse initial
v0x = v0 * np.cos(alphaRadians)
v0z = v0 * np.sin(alphaRadians)

print(f"v0x = {v0x:.2f} m/s")
print(f"v0z = {v0z:.2f} m/s")

#Tableaux de positions et vitesses
positions = np.array([
    [0.00],[0.00] # Le premier je stocke les positions en x, le deuxième pour stocker des positions en z
])
vitesse = np.array([
    [round(v0x, 2)],[round(v0z, 2)] # Le premier --> vitesse en x, deuxième --> vitesse en z
])

print(
    f"La position et la vitesse initial par rapport à l'axe horizontal x sont : {positions[0,0]} m, {vitesse[0,0]} m/s\n"
    f"La position et la vitesse initial par rapport à l'axe vertical z sont : {positions[1,0]} m, {vitesse[1,0]} m/s"
)

# Tableau de temps
tempsMax = 100
tempsACalculer = np.arange(dt,tempsMax,dt) # de 1s à 59s
print(f"Les calculs seront effectuer dans interval de temps suivant : {tempsACalculer[0]} s à {tempsACalculer[-1]} s")

# Calcul de positions
for temp in tempsACalculer:
    xi = v0x * temp
    zi = -0.5*g*temp**2 + v0z*temp

    if zi < 0:
        break

    positions = np.append(positions, [
        [round(xi, 2)], [round(zi, 2)]
    ], axis=1)
print(positions)

# Afficher la position à l'impact
positionImpact = positions[0,-1]
print(f"La position du boulet à l'impact est : {positionImpact} m ")

# Hauteur maximal
hauteurMax = np.argmax(positions[1,:])
print(f"Le boulet a atteint un hauteur maximal de : {hauteurMax} m")