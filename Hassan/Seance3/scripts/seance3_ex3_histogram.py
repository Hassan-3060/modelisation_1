import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(1000)
plt.figure()
plt.hist(data, bins = 100, color = 'gray')
plt.xlabel("data")
plt.ylabel("frequency")
plt.title("Histogram")
plt.legend(['Valeur random'])
plt.savefig('../figures/fig_s3ex3_hist.png')
plt.show()
