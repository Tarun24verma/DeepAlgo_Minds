# a=[9,4,9,8,4]
# set1=set(a)
# print(set1)
# b=[4,9,5]
# set2=set(b)
# print(list(set1.intersection(set2)))
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))