##3가지 과목(국어, 영어, 수학)에서의 각 학생의 성적을 딕셔너리에 저장. 학생의 이름(문자열)이 키(key)가
##되고 해당 학생의 성적이 포함된 정수 리스트가 값이 된다. 딕셔너리에서 각 학생의 성적을 꺼내서 각
##학생들의 평균 성적을 계산해서 출력
##- 생각하기 : 성적 딕셔너리 입력 및 출력(score_dic), for문(score_dic.items()), sum/len
score_dic ={'Kim': [99, 83, 95], 'Lee': [68, 45, 78], 'Choi': [25, 56, 69]}
for i in score_dic.keys():
    print(i,"의 평균성적=",sum(score_dic[i])/len(score_dic[i]))
    