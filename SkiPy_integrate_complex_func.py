from scipy import integrate
import numpy as np


def func(x, a):
    f = (np.exp(x / a) + np.exp(-x / a)) ** 2
    return np.pi * f


result = integrate.quad(func, 0, 5, args=(3,))

print(result)