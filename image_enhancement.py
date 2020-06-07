import cv2
import numpy as np

img = cv2.imread("lena.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.imshow("img",img)
# 平滑模板
fi1 = 1/9*np.array([[1,1,1],
                [1,1,1],
                [1,1,1]])
p1 = cv2.filter2D(gray,-1,fi1)
cv2.imshow("p1",p1)
#高斯
fi2 = 1/16*np.array([[1,2,1],
                [2,4,2],
                [1,2,1]])
p2 = cv2.filter2D(gray,-1,fi2)
cv2.imshow("p2",p2)
#梯度锐化
fi3 = np.array([[2,-1],
                [-1,0]])
p3 = cv2.filter2D(gray,-1,fi3)
cv2.imshow("p3",p3)
#laplacian
fi4 = np.array([[0,-1,0],
                [-1,4,-1],
                [0,-1,0]])
p4 = cv2.filter2D(gray,-1,fi4)
cv2.imshow("p4",p4)
#高通滤波
fi5 = np.array([[0,-1,0],
                [-1,5,-1],
                [0,-1,0]])
p5 = cv2.filter2D(gray,-1,fi5)
cv2.imshow("p5",p5)
#prewitt算子，sobel算子？有方向的检测

#伪彩色,灰度分层
#print(img)
blue = [0,0,255]
magenta = [0,255,255]
green = [0,255,0]
red = [255,0,0]
gray2color = []
for i in range(gray.shape[0]):
    row = []
    for j in range(gray.shape[1]):
        if gray[i][j]<63:
            row.append(blue)
        elif gray[i][j]<127:
            row.append(magenta)
        elif gray[i][j]<191:
            row.append(green)
        else:
            row.append(red)
    gray2color.append(row)
gray2 = np.array(gray2color,np.uint8)
cv2.imshow("gray2color",gray2)
# 伪彩色 映射函数

# 假彩色，绿色提高分辨率，蓝色敏感，提高观察到的色彩数

#频域滤波，平滑去除高频，锐化去除低频