import cv2
import numpy as np

img = cv2.imread('cat.png')
height,width,channel = img.shape

# 声明新的维度
new_dimension = (400, 400)
# 指定新图片的维度与插值算法（interpolation）
resized = cv2.resize(img, new_dimension, interpolation = cv2.INTER_AREA)

cv2.imwrite('cat_resize_400_400.png', resized)