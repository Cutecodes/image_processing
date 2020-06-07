import cv2
import numpy as np

img = cv2.imread("lena.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("lena",img)
cv2.imshow("lena",gray)

# x+128,y+128
def translation(x,y,dx,dy):
    trans = np.array([[1,0,0],[0,1,0],[dx,dy,1]])
    aftertrans = np.dot(np.array([x,y,1]),trans)
    return aftertrans[0],aftertrans[1]


imgtrans = np.zeros(img.shape, dtype = np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x,y = translation(i,j,128,128)
        if (x>=0)&(y>=0)&(x < img.shape[0])&(y<img.shape[1]):
            imgtrans[x][y] = img[i][j]
cv2.imshow("x+128,y+128",imgtrans)

# size/2

imgtrans2 = np.zeros((img.shape[0]//2,img.shape[1]//2,img.shape[2]), dtype = np.uint8)
for i in range(imgtrans2.shape[0]):
    for j in range(imgtrans2.shape[1]):
        imgtrans2[i][j] = img[2*i][2*j]
cv2.imshow("size/2",imgtrans2)

# size*2 线性插值

imgtrans3 = np.zeros((img.shape[0]*2,img.shape[1]*2,img.shape[2]), dtype = np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(j+1<img.shape[1])&(i+1<img.shape[0]):
            imgtrans3[2*i][2*j] = img[i][j]
            imgtrans3[2*i+1][2*j] = img[i][j]//2+img[i+1][j]//2
            imgtrans3[2*i][2*j+1] = img[i][j]//2+img[i][j+1]//2
            imgtrans3[2*i+1][2*j+1] = img[i][j]//4+img[i+1][j+1]//4+img[i+1][j]//4+img[i][j+1]//4
cv2.imshow("size*2",imgtrans3)
