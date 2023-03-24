from scipy import integrate
import numpy as np

result = integrate.quad(lambda x: 1/x, 1, np.inf)
print(result)
