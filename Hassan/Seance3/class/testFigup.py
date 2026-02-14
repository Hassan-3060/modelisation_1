from Figup import *
import numpy as np

x = np.linspace(-5,5,15)
y = x**2
z = np.sqrt(y)
w = z**3
colors = ['red', 'green', 'blue']

fig = Figup(x, y, colors[0], 'Courbe de Figup', 'y = x²', 'x, y')
#fig.ajouterCourbe(y, z, colors[1], 'z =  $\\sqrt{y}$').ajouterCourbe(z, w, colors[2], 'w = $z^3$').courbe()

fig2 = Figup(x, y, colors[0], 'Courbe de Figup 2', 'y = x²', 'x, y')
#fig2.ajouterCourbe(y, z, colors[1], 'z =  $\\sqrt{y}$').courbe()

fig3 = Figup(w, z, colors[0], None, 'w = $z^3$', 'w, z')
#fig3.courbe()

fig4 = Figup(w, z, colors[0], legend='w = $z^3$', title = 'courbe w et z')
fig4.courbe()