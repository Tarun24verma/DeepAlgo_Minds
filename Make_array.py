def solve (N, A):
    B=[0]*N
    C=[]
    confiedence=0
    for i in range(N-15):
        if A[i]==B[i]:
            confiedence+=1
        else:
            C.append(i)
    if confiedence==0:
        return -1
    else:
        for i in C:
            while B[i]!=A[i]:
                B[i]+=1
    return B
    pass
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print (out_)