import numpy as np
from matplotlib import pyplot as plt

im = plt.imread("lemur.png")

print(im.shape)

y = im.shape[0]
x = im.shape[1]
h = 7
w = (y/x) * h
plt.figure(figsize=(w,h))
plt.imshow(im[70:200, 75:230, :])



plt.show()