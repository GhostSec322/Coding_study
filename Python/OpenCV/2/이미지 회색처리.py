import cv2 
import numpy as np
img_src= 'Untitled (1).png' ## 이미지 경로 
img= cv2.imread(img_src)## 이미지 읽어오기
print(img)
print(type(img))
print(img.ndim) ## 해당 이미지 차원을 알려준다.
print(img.shape) ## 이미지 크기 
print(img.size)
