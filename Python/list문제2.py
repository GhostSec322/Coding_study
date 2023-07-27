data=[] ##빈리스트
i=1
x= int(input(f"{i}일차 턱걸이 횟수>>"))
i+=1
data.append(x)
x= int(input(f"{i}일차 턱걸이 횟수>>"))
i+=1
data.append(x)
x= int(input(f"{i}일차 턱걸이 횟수>>"))
i+=1
data.append(x)
x= int(input(f"{i}일차 턱걸이 횟수>>"))
i+=1
data.append(x)
x= int(input(f"{i}일차 턱걸이 횟수>>"))
i+=1
data.append(x)
x= int(input(f"{i}일차 턱걸이 횟수>>"))
i+=1
data.append(x)
x= int(input(f"{i}일차 턱걸이 횟수>>"))
data.append(x)
print(data)
result= data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]
print(int(result/len(data)))
