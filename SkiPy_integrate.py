from scipy import integrate
import numpy as np

result = integrate.quad(lambda x: np.sin(x), 0, np.pi)
print(result)