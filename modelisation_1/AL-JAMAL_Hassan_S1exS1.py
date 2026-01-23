"""
AL JAMAL HASSAN
L1 Physique
Groupe 250A
"""

# Section import
import numpy as np

# EX S1.1
a = [1,2,3,4,5]
moyenne = sum(a)/len(a) #Il faut stocker l'opération dans une variable
print(f"EX S1.1\nLa moyenne est de {moyenne}\n-------") # Ici j'affiche la valeur de la variable

# EX S1.2
angles = [0,30,45,60,90]
valeurCosinus = np.cos(np.radians(angles)) # La bib numpy fait les calculs en radians. Il existe une fonction np.radians qui convertis les valeurs en degrés
print(f"EX S1.2\n{valeurCosinus}\n-------")

# EX S1.3
# Je fais avec une fonction, simple et rapide
def NombresPremiers(seuil : int):
    '''
    :param seuil: Jusqu'à quel nombre je veux vérifier
    :return: Une liste contient les nombres premiers jusqu'à le seuil
    '''
    nombresPremiers = [] # crée une liste vide, afin de stocker les nombres premiers durant les calculs
    for nombre in range(2, seuil+1):
        EstPremier = True # au début je suppose que chaque nombre est premier
        for i in range(2, nombre):
            if nombre % i == 0: # Ici je vérifie si nombre est divisible par un nombre autre que 1 et lui même. Dans la condition je laisse donc nombre et non nombre+1
                EstPremier = False # Si la condition est validé ( le reste est égale à 0), donc le nombre n'est pas premier
        if EstPremier: # Si vrai -> i.e, le nombre est premier
            nombresPremiers.append(nombre) # J'ajoute le nombre à la liste
    return nombresPremiers # Je retourne la liste
print(f"EX S1.3\n{NombresPremiers(100)}\n-------")

# EX S1.4
def Euclidien(a : int, b : int):
    """
    Une fonction qui calcul les quotient et le reste entre deux valeurs
    :param a: Un nombre entier
    :param b: le diviseur (b < 0)
    :return: un tuple (q -> quotient, r -> reste)
    """
    q = 0
    r = a
    while r >= b: # tant que le reste est supérieure ou égale à b, on reste dans la boucle
        r = r - b
        q += 1
    return q, r
quotient, reste = Euclidien(30, 7) # je declare deux variables, quotient prend la valeur de q retourner en premier dans la fonction; et reste prend la valeur de r
print(f"EX S1.4\nLa division de 30 par 7 donne :\nQuotient = {quotient}\nReste = {reste}\n-------")