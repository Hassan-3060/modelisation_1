from email.charset import add_alias

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
tMax = 100

# Composantes de v0x et v0z de la vitesse initial
v0x = v0 * np.cos(alphaRadians)
v0z = v0 * np.sin(alphaRadians)

# Estimation du nombre de points à calculer
nombrePoints = int(tMax / dt)

# Tableaux de positions et vitesses
positions = np.zeros((2, nombrePoints))

vitesse = np.zeros((2, nombrePoints))
vitesse[0,0] = v0x
vitesse[1,0] = v0z

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

acceleration = np.zeros((2, nombrePoints))

## Calculs automatique
#while  positions[1,-1] >= 0 :
dernierIndice = 0 # pour connaître le dernier indice calculé et éviter de garder les valeurs nulles
for i in range(1, nombrePoints):
    vitesseEnX = vitesse[0 ,i-1]
    vitesseEnZ = vitesse[1 ,i-1]

    positionEnX = positions[0 ,i-1]
    positionEnZ = positions[1 ,i-1]

    acceleration[0, i], acceleration[1,i] = accelerationCalcul(vitesseEnX, vitesseEnZ)
    vitesse[0, i], vitesse[1, i] = vitesseSuivant(vitesseEnX, vitesseEnZ, acceleration[0, i], acceleration[1, i])
    positions[0, i], positions[1, i] = positionSuivante(positionEnX, positionEnZ, vitesse[0,i], vitesse[1,i])

    if positions[1, i] < 0:
        dernierIndice = i
        break
    dernierIndice = i

positions = positions[:, :dernierIndice]
vitesse = vitesse[:, :dernierIndice]
acceleration = acceleration[:, :dernierIndice]

# Hauteur max
maxHauteur = np.max(positions[1 ,:])
#Impact
valeurImpact = np.max(positions[0 ,:])
# Distance à la hauteur max
indiceMaxHauteur = np.argmax(positions[1 ,:])
distanceMaxHauteur = positions[0, indiceMaxHauteur]

print(f"La hauteur maximal atteint par le boulet est : {maxHauteur:.2f}, et le valeur d'impacte est : {valeurImpact:.2f}\nLa distance à la hauteur max est : {distanceMaxHauteur:.2f}")

# Partie affichage
plt.figure()
plt.scatter(positions[0,:], positions[1,:], color='red', marker='o', label='data')
plt.title('Trajectoire du boulet de canon avec frottements')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.savefig('fig_s3ex5_tir.png')
plt.show()