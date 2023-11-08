score=[] #점수 저장리스트 선언
i=0
while i <5:
    a=float(input("성적을 입력하세요:"))
    score.append(a)
    i+=1

print("성적 평균: ",(sum(score)/len(score)))
print("최고점수: ",max(score))
print("최저점수: ",min(score))
print("80점 이상 받은 학생 :", score.count(80))