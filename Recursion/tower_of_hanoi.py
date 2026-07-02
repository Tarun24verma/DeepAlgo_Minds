n=3
i=1
m=1
def tot(n,m,i):
    if n==0: return 0
    if i==n: 
        return m
    return tot(n,(m*2)+1,i+1)
print(tot(n,m,i))
# class Solution:
#     def  towerOfHanoi(self, n, fromm, to, aux):
#         i=1
#         m=1
#         def tot(n,m,i):
#             if n==0: return 0
#             if i==n: 
#                 return m
#             return tot(n,(m*2)+1,i+1)
#         return(tot(n,m,i))
# m=0
# def Tower_of_hanoi(n,start_rod,helping_rod,target_rod,m):
#     global m
#     if n==0:
#         return
#     Tower_of_hanoi(n-1,start_rod,target_rod,helping_rod,m)
#     print(f"Move disk from {start_rod} to {target_rod}")
#     m+=1
#     Tower_of_hanoi(n-1,helping_rod,start_rod,target_rod,m)
# n=3
# Tower_of_hanoi(n,"A","b","c",m=0)
# print(m)
