import numpy as np
import cv2 


def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g


print(gaussian_kernel(5))

img = cv2.imread('C:/Users/student/Desktop/emma.png')
cv2.imshow(img)
    