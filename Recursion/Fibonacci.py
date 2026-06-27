def add_f(a,b):
    return a+b
a=[0,1]
for i in range(1,9):
    a.append(a[i-1]+a[i])
    print(a[i+1])
print(a)