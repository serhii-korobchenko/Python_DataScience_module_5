import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

im = plt.imread("lemur.png")

rotate_face = ndimage.rotate(im, -45)

plt.imshow(rotate_face)
plt.show()