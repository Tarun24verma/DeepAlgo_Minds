def sub(a,i):
    if i>len(a):
        return None
    k=0
    while k<len(a):
        print(a[k:k+i])
        k+=1
    sub(a,i+1)
sub("abccba",1)