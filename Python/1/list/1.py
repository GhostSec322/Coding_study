animals =['사자','호랑이','고양이','강아지']

for i in range(len(animals)):
    print(i,"번 인덱스 동물:",animals[i])

### list 데이터 추가 :마지막에 값을 추가
animals.append("뱀")
print("    ")
for i in range(len(animals)):
    print(i,"번 인덱스 동물:",animals[i])
### 데이터 삭제
del animals[0] ## 0번쨰 값 

print("    ")
for i in range(len(animals)):
    print(i,"번 인덱스 동물:",animals[i])

##슬라이싱
print("     ")
print(animals[0:2])
## 길이 
print(len(animals))
## 정렬
animals.sort(reverse=True)
print(animals)
animals.sort()
print(animals)