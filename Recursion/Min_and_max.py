def MinMax(arr,n,m):
    if arr[0]>m:
        m=arr[0]
    if arr[0]<n:
        n=arr[0]
    if arr[0]==arr[-1]:
        return n,m
    n,m=MinMax(arr[1:],n,m)
    return n,m
arr=[1,2,3,4,5,6,7,8]
a=list(MinMax(arr,arr[0],arr[0]))
print(a)