animals=["사자","호랑이","뱀","강아지","고양이"]
animals.append("말")## 데이터 추가
print(animals)
animals[2]="하이에나"## 데이터 수정
del animals[5]## 데이터 삭제
print(animals)
print(animals[1:4])## 데이터 슬라이싱
print(animals[:])## list 전체 출력
print(animals[:3])## list 데이터 앞에서 부터 3개만 출력
print(animals[2:])## list 2번째 인덱스부터 출력
print(animals[-1])## list 마지막 데이터 출력
print(animals)
animals.sort(reverse=True)
print(animals)