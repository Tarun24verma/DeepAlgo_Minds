class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a=b=0
        for i in set(nums):
            a+=i*3
        b=sum(nums)
        return (a-b)//2
