i=int(input())
def conv(i):
    if i==0:
        return ""
    else:
        return conv(i//2)+str(i%2)
print(conv(i))