import cv2 
img_src= '1\home.png' ## 이미지 경로 
img1= cv2.imread(img_src,-1)## 이미지 읽어오기
img2= cv2.imread(img_src,0)## 이미지 읽어오기
img3= cv2.imread(img_src,1)## 이미지 읽어오기
#cv2.IMREAD_GRAYSCALE(0) : 흑백
#cv2.IMREAD_UNCHANGED(-1):
#cv2.IMREAD_COLOR(1):컬러
cv2.imshow('Home1',img1)## 이미지 출력하기
cv2.imshow('Home2',img2)## 이미지 출력하기
cv2.imshow('Home3',img3)## 이미지 출력하기
cv2.waitKey(0)## 키보드 입력 대기
cv2.destroyAllWindows()## 윈도우 창 닫기