from scipy.interpolate import interp2d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
z = np.linspace(0, 100, 100)

print(len(x))
X, Y = np.meshgrid(x, y)

px, py, pz = np.random.choice(x, 50), np.random.choice(y, 50), np.random.choice(z, 50)
print(len(px))
f = interp2d(px, py, pz, kind='cubic')

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, f(x,y))

plt.show()