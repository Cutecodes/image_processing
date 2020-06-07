import cv2
import numpy as np

img = cv2.imread("test2.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.imshow("img",img)

# 灰度阈值分割
T = 0
dt = 0
while True:
    num1 = 0
    num2 = 0
    g1 = 0
    g2 = 0
    u1 = 0
    u2 = 0
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            if gray[i][j]>T:
                num1 = num1 + 1
                g1 = g1 + gray[i][j]
            else:
                num1 = num1 + 1
                g1 = g1 + gray[i][j]
    if num1!=0:
        u1 = g1 // num1
    if num2!=0:
        u2 = g2 // num2
    t = (u1 + u2)//2
    if abs(t-T)==0:
        break
    T = t

gray2 = np.zeros(gray.shape, dtype = np.uint8)
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i][j]>T:
            gray2[i][j]=255
cv2.imshow("fenge",gray2)