import cv2 
import numpy as np

img_src = 'Untitled (1).png'  ## 이미지 경로 
img = cv2.imread(img_src)  ## 이미지 읽어오기
img_dst = img.astype(np.uint16)  ## 16비트로 이미지 변환
b, g, r = cv2.split(img_dst)
gray = ((b + g + r) / 3).astype(np.uint8)  ## 회색

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.waitKey(0)  # 이미지가 표시되는 시간 (0이면 무한대기)
cv2.destroyAllWindows()  # 창 닫기
