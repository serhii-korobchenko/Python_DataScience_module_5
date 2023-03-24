import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

im = plt.imread("lemur.png")


blurred_im_2 = ndimage.gaussian_filter(im, sigma=0.5)
blurred_im_4 = ndimage.gaussian_filter(im, sigma=1)

fig, axs = plt.subplots(1, 3, figsize=(20,40))

axs[0].imshow(im)
axs[1].imshow(blurred_im_2)
axs[2].imshow(blurred_im_4)

plt.show()