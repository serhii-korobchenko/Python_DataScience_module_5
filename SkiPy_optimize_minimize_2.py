from scipy.interpolate import griddata
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000)
y = np.linspace(-10, 10, 10000)
X, Y = np.meshgrid(x, y)

px, py = np.random.choice(x, 2500), np.random.choice(y, 2500)

def f(arg):
    x, y = arg
    return x ** 2  * y ** 2 + 2

z = griddata((px, py), f((px, py)), (X, Y), method='cubic')
plt.contour(x, y, z)

result = minimize(f, [-10, -10],  method='Nelder-Mead')
print(result)

plt.show()
