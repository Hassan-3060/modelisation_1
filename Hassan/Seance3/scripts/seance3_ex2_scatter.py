import os

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 20)
y = np.random.rand(20)
data = np.column_stack((x, y))
np.savetxt('../fichiers/data.txt', data, header='x, y', fmt='%.4f')

dataImporter = np.loadtxt('../fichiers/data.txt')
xImporter = dataImporter[:,0]
yImporter = dataImporter[:,1]

plt.figure()
plt.scatter(xImporter, yImporter, color='red', marker='o', label='data')
plt.title('Nuage de points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('../figures/fig_s3ex2_scatter.png')
plt.show()
