score=[] #점수 저장리스트 선언
i=0
up_score_80=0; ## 80점 이상 학생 수 
while i <5:
    a=float(input("성적을 입력하세요:")) ## 사용자로부터 입력을 받는다
    score.append(a)## score 리스트에 추가한다.
    if(score[i]>=80):## 80점 이상인 학생이 있을시 실행하는 조건문이다
        up_score_80 +=1 ## 80점 이상 학생수를 1 증가 시킨다
    i+=1

print("성적 평균: ",(sum(score)/len(score)))## 평균을 구해서 출력한다
print("최고점수: ",max(score)) ## max함수를 이용해서 최고점수를 구해서 출력한다
print("최저점수: ",min(score)) ## min함수를 이용하여 최저점수를 구해서 출력한다.
print("80점 이상 받은 학생 :",up_score_80) ## 80점 이상학생 수를 출력한다. 
