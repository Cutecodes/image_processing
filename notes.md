## 基础变换  
1. 数字直方图：统计各灰度出现频次，体现对比度，动态范围、亮度等信息，均匀分布较好。  
2. 直方图均衡化：通过灰度映射，对灰度图进行改造：可采用分布函数和灰度值就近匹配  
3. 灰度变换：对比度：最亮/最暗，灰度变换，对每个像素逐个变换：加减常数（改变亮度）、图像反转（255-灰度值）、乘除常数（对比度）、分段函数（削波）二值窗口、非线性变换、查表等  
4. 图像运算：算术和逻辑
+ 算术运算：加法（去除叠加噪声，叠加），减法（同一场景的变化、特效），乘法（局部显示，二值蒙版）  
+ 逻辑运算：与或非，常用二值图像  
5. 图像几何变换：平移、镜像、转置、旋转、缩放、拉伸（控制点）  
6. 插值：最近邻插值、双线性插值、三次立方插值、  
7. 正交变换：将图像分解成基图像  
8. 离散傅里叶变换：

## 图像增强
1. 空域平滑：领域模板  
+ 去除噪声  
+ 加大卷积模板加大滤波程度，但更模糊  
+ 高斯平滑，权不同  

## 分割  
1. 基于不连续性和相似性：边界分割法，门限分割法，面向区域分割法、模板匹配分割法等  
2. 边缘检测：各种算子，边缘不闭合的处理  
3. 基于区域：区域生长法，  

## 数学形态处理  
1. 膨胀与腐蚀  
2. 开运算与闭运算  