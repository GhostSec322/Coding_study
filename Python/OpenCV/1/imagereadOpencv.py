import cv2 
img_src= '1\home.png' ## 이미지 경로 
img= cv2.imread(img_src)## 이미지 읽어오기
cv2.imshow('Home',img)## 이미지 출력하기
cv2.waitKey(0)## 키보드 입력 대기
cv2.destroyAllWindows()## 윈도우 창 닫기