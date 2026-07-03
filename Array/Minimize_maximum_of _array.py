import math
class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        prefix_sum=0
        ans=0
        for i, num in enumerate(nums,1):
            prefix_sum+=num
            if ans*i<prefix_sum:
                ans=math.ceil(prefix_sum/i)
        return ans