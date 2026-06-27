def pal(a,s,e):
    if s<=e:
        if a[s]==a[e]:
            if s//2==len(a)//2:
                return True
            return pal(a,s+1,e-1)
        else:
            if s==(len(a)//2)+1:
                return True
            return False
    else: return True

a="abcba"
s=0
e=len(a)-1
print(pal(a,s,e))