import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as pc
from scipy.optimize import minimize_scalar, leastsq, curve_fit, brentq

x = np.linspace(-5, 5, 50)
y = x ** 2 + 3 * x - 4
plt.grid()
plt.plot(x, y)
plt.axhline(linewidth=1, color='b')
plt.axvline(linewidth=1, color='b')

def f(x):
    return x ** 2 + 3 * x - 4

left_root = brentq(f, -5, 0)  # -4
rigth_root = brentq(f, 0, 5)  # 1

print(left_root, rigth_root)

plt.show()