# class Solution:
#     def findDuplicate(self, nums: list[int]) -> int:
#         mem=set()
#         for i in nums:
#             if i in mem:
#                 return i
#             mem.add(i)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        mem=[0]*len(nums)
        for i in nums:
            if mem[i]:
                return i
            mem[i]=1



























# l=[1,3,4,2,2]

# def check(l):
#     # # for i,e in enumerate(l):
#     # #     l.pop(i)
#     # #     if e in l[i+1:]:
#     # #         return l.pop(i)
#     # while l:
#     #     k=l.pop(0)
#     #     if k in l:
#     #         return k
#     mem=set()
#     for i in l:
#         if i in mem:
#             return i
#         mem.add(i)

# print(check(l))
# print(l)