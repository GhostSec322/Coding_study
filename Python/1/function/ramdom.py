import random
def random_num(a,b):
    rn=random.randint(a,b)
    return rn

x=[]
while len(x) < 6:

    num=random_num(1,45)
    if(len(x) ==6):
        break
    if(num in x):
        num =0
    else:
        x.append(num)
    
   
x.sort()       
print(x)