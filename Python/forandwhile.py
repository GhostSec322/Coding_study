data=[]
i=1
for k in range(0,7):

    x= int(input(f"{i}일차 턱걸이 횟수>>"))
    i+=1
    data.append(x)

result=0
j=0
for j in range(0,len(data)):
    result+=data[j-1]
print(int(result/len(data)))
