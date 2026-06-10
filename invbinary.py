i=input()
num=1
if i[len(i)-1]=='1':
    b=1
else:
    b=0
if int(i)==0:
    num=0
else:
    ind=0
    for j in i:
        if j=='1':
            break
        else:
            ind+=1
    k=i[ind+1:]            
    for j in range(len(k),0,-1):
        num*=2
print(num+b)