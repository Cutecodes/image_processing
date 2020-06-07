import cv2
import numpy as np

img = cv2.imread("lena.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

# +128
grayadd = np.empty(gray.shape, dtype = np.uint8)
for i in range(gray.shape[1]):
    for j in range(gray.shape[1]):
        if gray[i][j]+128>255:
            grayadd[i][j] = 255
        else:
            grayadd[i][j] = gray[i][j]+128        
cv2.imshow("gray+128",grayadd)

# -128
graysub = np.empty(gray.shape, dtype = np.uint8)
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i][j]-128<0:
            graysub[i][j] = 0
        else:
            graysub[i][j] = gray[i][j]-128        
cv2.imshow("gray-128",graysub)

# reverse
grayreverse = np.empty(gray.shape, dtype = np.uint8)
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        grayreverse[i][j] = 255 - gray[i][j]       
cv2.imshow("grayreverse",grayreverse)

# binaryzation
graybin = np.empty(gray.shape, dtype = np.uint8)
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i][j]<128:
            graybin[i][j] = 0
        else:
            graybin[i][j] = 255        
cv2.imshow("graybin",graybin)

