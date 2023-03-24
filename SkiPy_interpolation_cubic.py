import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

date = np.linspace(1, 8, 8)
day = [23, 17, 17, 16, 15, 14, 17, 20]

f = interp1d(date, day, kind='cubic')

plt.plot(date, day, 'o')
more_date = np.linspace(1, 8, 100)
plt.plot(more_date, f(more_date))
plt.ylim(0,25)
plt.show()