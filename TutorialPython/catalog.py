import os
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 7)
y = [2,2,5,3,9,7,25]
print(y)

where_set = ['pre', 'post', 'mid']
fig, axs = plt.subplots(1, 1, figsize=(15, 4))

axs.step(x, y, "g-o", where='post')
axs.grid()

plt.show()