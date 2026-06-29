a=[1,2]
def sums(a,ex):
    if ex==len(a)-1:
        return a
    ex+=1
    sums(a,ex)
    a[ex]=0
    print(sum(sums(a,ex)))
sums(a,ex=0)