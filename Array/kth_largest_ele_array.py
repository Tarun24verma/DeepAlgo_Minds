import numpy as np
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        r=len(nums)-k
        p=np.partition(nums,r)
        ans=int(p[r])
        return ans