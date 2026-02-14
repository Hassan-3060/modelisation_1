#imports
from turtledemo.penrose import star, main

import matplotlib.pyplot as plt
import numpy as np

# 1.1
x = np.linspace(-5,5,15)
y = x**2
z = np.sqrt(y)

execute = __name__ == "__main__"

## Afficher sur la même courbe
if not execute:
    plt.figure()
    plt.plot(x,y, color='red')
    plt.plot(x,z, color='blue')
    plt.legend(['y = x²', 'z =  $\\sqrt{y}$'])
    plt.show()

## Deux courbes
if not execute:
    plt.figure()
    plt.plot(x, y, color='red')
    plt.title('Courbe de x et y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['Courbe de x', 'Courbe de y'])
    plt.show()

    plt.figure()
    plt.plot(x, z, color='blue')
    plt.title('Courbe de x et z')
    plt.xlabel('x')
    plt.ylabel('z')
    plt.legend(['Courbe de x', 'Courbe de z'])
    plt.show()

# 1.2
start = -1
stop = 1
Nval = 11
step = 0.2
x = np.linspace(start,stop,Nval)
y = np.arange(start,stop + step/2,step)

# Tests avec asserts
assert np.shape(x)==np.shape(y)

if not execute:
    plt.figure()
    plt.plot(x,y, color='red')
    plt.title('Courbe de x et y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['Courbe de x', 'Courbe de y'])
    plt.show()
