class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result=[0]*len(nums)
        last_even=0
        last_odd=0
        for i in nums:
            if i<0:
                result[(2*last_odd)+1]=i
                last_odd+=1
            else: 
                result[2*last_even]=i
                last_even+=1
        return result