import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as pc
from scipy.optimize import minimize_scalar, leastsq

t = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([23, 17, 17, 16, 15, 14, 17, 20])

def parabola(t, a, b, c):
    return a * pow(t, 2) + b * t + c

def diff(p, y, t):
    a, b, c = p
    return y - parabola(t, a, b, c)

p0 = (1, 3, 4)
aprx, _ = leastsq(diff, p0, args=(y, t))
print(aprx)


y_p = aprx[0] * t ** 2 + aprx[1] * t + aprx[2]
plt.grid()
plt.plot(t, y, label='data')
plt.plot(t, y_p, label='MNK')
plt.legend()

plt.show()
