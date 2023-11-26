result={
    "승리여부":"승리",
    "Champ_name": '비에고',
    'kill':13,
    'death':9,
    'assist':13
}
## 딕셔너리 접근
print(result['승리여부'])
## 딕셔너리 수정
result['승리여부']='패배'
## 새로운 키, 값 추가
result['level']=100
## 데이터 삭제
del result['Champ_name']
print(result)

## 딕셔너리 함수
##keys()
for i in result.keys():
    print(i)
##values()
for i in result.values():
    print(i)

## items()
for k,v in result.items():
    print(k,':',v)