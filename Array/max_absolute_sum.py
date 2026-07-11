class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        cur_max,max_till_now,cur_min,min_till_now=0,0,0,0
        for i in nums:
            cur_max=max((i),(i+cur_max))
            max_till_now=max(cur_max,max_till_now)
            cur_min=min(i,i+cur_min)
            min_till_now=min(cur_min,min_till_now)
        min_till_now=abs(min_till_now)
        return max(max_till_now,min_till_now)


# import math

# nums=[2,-5,1,-4,3,-2]
# cur_max=0
# max_till_now=-math.inf
# check=[]
# for i in nums:
#     check.append(abs(cur_max))
#     cur_max=max(abs(i),abs(i+cur_max))
#     max_till_now=max(cur_max,max_till_now)
# print(max_till_now)
# print(check)