import cv2 
img_src= 'home.png' ## 이미지 경로 
img_dst="Home_result.png"
img= cv2.imread(img_src,cv2.IMREAD_GRAYSCALE)## 이미지 읽어오기
if img is not None:
    cv2.imshow('Home',img)## 이미지 출력하기
    cv2.imwrite(img_dst,img)
else:
    print("이미지를 불러오지 못 했습니다.")
cv2.waitKey(0)## 키보드 입력 대기
cv2.destroyAllWindows()## 윈도우 창 닫기