a='qwertyuiop'
# point=0
# def length(a,point):
#     if a[point:]=="":
#         print(point)
#         return
#     point+=1
#     length(a,point)

# length(a,point)

def length(a):
    if a=="":
        return 0
    return 1+length(a[1:])
print(length(a))