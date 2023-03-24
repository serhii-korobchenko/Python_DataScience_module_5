import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = [-1, 1, 3]
y = [2, 12, 54]
f = interp1d(x, y, kind='quadratic')
plt.plot(x, y, 'o')
more_x = np.linspace(-1, 3, 100)
plt.plot(more_x, f(more_x), 'g')
plt.show()