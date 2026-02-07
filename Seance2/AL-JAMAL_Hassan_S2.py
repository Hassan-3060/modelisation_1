
# Import
import numpy as np
import matplotlib.pyplot as plt
# Initialisation
v0 = 450
alpha = 45
alphaRadians = np.radians(alpha)
g = 9.81
m = 18
dt = 0.1
k = 0.3

# Composantes de v0x et v0z de la vitesse initial
v0x = v0 * np.cos(alphaRadians)
v0z = v0 * np.sin(alphaRadians)

# Tableaux de positions et vitesses
positions = np.array([
    [0.00] ,[0.00] # Le premier je stocke les positions en x, le deuxième pour stocker des positions en z
])
vitesse = np.array([
    [round(v0x, 2)] ,[round(v0z, 2)] # Le premier --> vitesse en x, deuxième --> vitesse en z
])

print(
    f"La position et la vitesse initial par rapport à l'axe horizontal x sont : {positions[0 ,0]} m, {vitesse[0 ,0]} m/s\n"
    f"La position et la vitesse initial par rapport à l'axe vertical z sont : {positions[1 ,0]} m, {vitesse[1 ,0]} m/s"
)

# Calcul de positions en tenir compte de frottements
## Fonctions de calculs d'accélérations, vitesse et positions en prenant en compte les frottements
def accelerationCalcul(vitesseEnX, vitesseEnZ):
    ax = -( k /m ) * vitesseEnX * np.sqrt(vitesseEnX**2 + vitesseEnZ**2)
    az = - g -( k /m ) * vitesseEnZ * np.sqrt(vitesseEnX**2 + vitesseEnZ**2)

    return ax, az

def vitesseSuivant (vitesseEnX : float ,vitesseEnZ : float, accelerationEnX : float, accelerationEnZ):
    vx = vitesseEnX + accelerationEnX * dt
    vz = vitesseEnZ + accelerationEnZ * dt
    return vx, vz

def positionSuivante(positionEnX: float, positionEnZ : float, vitesseEnX: float, vitesseEnZ: float):
    x = positionEnX + vitesseEnX * dt
    z = positionEnZ + vitesseEnZ * dt
    return x, z

acceleration = np.array([[],[]])
## Calculs automatique
while  positions[1,-1] >= 0 :

    vitesseEnX = vitesse[0 ,-1]
    vitesseEnZ = vitesse[1 ,-1]

    positionEnX = positions[0 ,-1]
    positionEnZ = positions[1 ,-1]

    ax, az = accelerationCalcul(vitesseEnX, vitesseEnZ)
    acceleration = np.append(acceleration, [[ax] ,[az]], axis = 1)

    vx, vz = vitesseSuivant(vitesseEnX, vitesseEnZ, ax, az)
    vitesse = np.append(vitesse, [[vx] ,[vz]], axis = 1)

    x, z = positionSuivante(positionEnX, positionEnZ, vx, vz)
    positions = np.append(positions, [[x] ,[z]], axis = 1)

# Hauteur max
maxHauteur = np.max(positions[1 ,:])
#Impact
valeurImpact = np.max(positions[0 ,:])

print(f"La hauteur maximal atteint par le boulet est : {maxHauteur:.2f}, et le valeur d'impacte est : {valeurImpact:.2f}")

# Partie affichage
plt.figure()
plt.plot(positions[0 ,:], positions[1 ,:], label="Trajectoire")
plt.xlabel("Distance (m)")
plt.ylabel("Hauteur (m)")
plt.title("Trajectoire du projectile")
plt.legend()
plt.grid(True)
plt.show()