def add_a(a,s,e):
    if s>e:
        return "out of range"
    if s==e:
        return a[s]
    return a[s]+add_a(a,s+1,e)
a=[8,1,2,3,4,5]
print(add_a(a,6,5))