import os
import numpy as np
import matplotlib.pyplot as plt
import cv2.cv2 as cv2


images = [f for f in os.listdir('images')]
labels = [f for f in os.listdir('labels')]
pairs = []
for i in range(len(images)):
    im = cv2.imread('images\\' + images[i])
    if isinstance(im, np.ndarray):
        print(im[0])
        im = np.apply_along_axis(lambda x: np.apply_along_axis(lambda y: [y[2], y[1], y[0]], 1, x), 1, im)
    plt.imshow(im)
print()