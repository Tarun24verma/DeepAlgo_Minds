# k=int(input())
# t=k
# if k%2==1:
#     print(k-1)
# else:
#     b=0
#     while t%2==0:
#         b+=1
#         t=t//2
#     print(k-(2**(b)))
ans=[]
a=int(input())
pos = 0
while a:
    if a&1==1:
        ans.append(pos)
    a=a>>1
    pos+=1
print(ans)