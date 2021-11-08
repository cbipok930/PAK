import os
import numpy as np
import matplotlib.pyplot as plt
import cv2.cv2 as cv2


images = [f for f in os.listdir('images')]
labels = [f for f in os.listdir('labels')]
pairs = []
for i in range(len(images)):
    im = cv2.imread('images\\' + images[i])
    mask = cv2.imread('labels\\' + labels[i])
    if isinstance(im, np.ndarray):
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        pairs.append((im, mask))
        plt.subplot(3, 2, (2*i) % 6 + 1)
        plt.imshow(pairs[i][0])
        plt.subplot(3,2, (2*i) % 6 + 2)
        plt.imshow(pairs[i][1])
    if i % 3 == 0 and i != 0:
        plt.show()
    for j in range(3):
        maps = ["Reds", "Greens", "Blues"]
        image_out = im.copy()
        plt.subplot(1, 3, j + 1)
        plt.imshow(image_out[:, :, j] * -1, cmap=maps[j])
    plt.imshow(u)
print()