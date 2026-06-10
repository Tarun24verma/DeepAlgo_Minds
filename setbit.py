def conv(i):
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
    return num+b
i=int(input())
count=0
setbit=[]
while i>0:
    if i&1==1:
        count+=1
        setbit.append(1)
    else:
        setbit.append(0)
    i//=2
print(count)
print(setbit)
j=int(input())
if j>=len(setbit):
    print("unset bit")
else:
    if setbit[j]==1:
        print("set bit")
    else:
        print("unset bit")
k=int(input())
if k>=len(setbit):
    setbit.extend([0]*(k-len(setbit)+1))
setbit[k]=1
print(setbit)
l=''.join(map(str, reversed(setbit)))
print(conv(l))

