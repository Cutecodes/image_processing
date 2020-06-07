import cv2
import numpy as np

img = cv2.imread("lena.jpg")
img2 = cv2.imread("test.jpg")

#add
imgadd = np.empty(img.shape, dtype = np.uint8)
imgadd = img//2 + img2//2

cv2.imshow("imgadd",imgadd)
