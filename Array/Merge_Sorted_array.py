class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p=m+n-1
        m-=1
        n-=1
        while n>=0:
            if m>=0 and nums1[m]>nums2[n]:
                nums1[p]=nums1[m]
                m-=1
            else:
                nums1[p]=nums2[n]
                n-=1
            p-=1












# nums1 = [4,5,6,0,0,0]
# m=3
# nums2 = [1,2,3]
# n=3
# # while len(nums2)!=0:
# #     nums1[n-len(nums2)]=nums2.pop(0)
# # print(nums1)
# # # for i in range(len(nums1)-1):
# # #     if nums1[i]>nums1[i+1]:
# # #         nums1[i],nums1[i+1]=nums1[i+1],nums1[i]
# # # print(nums1)
# # def listsort(nums1):
# #     change=0
# #     for i in range(len(nums1)-1):
# #         if nums1[i]>nums1[i+1]:
# #             nums1[i],nums1[i+1]=nums1[i+1],nums1[i]
# #             change=1
# #     if change:
# #         listsort(nums1)
# #     return
# def merge_sort(nums1,nums2,m,n):
#     if nums2:
#         t=nums2.pop(0)
#         for i in range(len(nums1)):
#             if nums1[i]>t:
#                 nums1[i],t=t,nums1[i]
#             if nums1[i]==0:
#                 nums1[i]=t
#         merge_sort(nums1,nums2,m,n)
#     return

# merge_sort(nums1,nums2,m,n)
# print(nums1)   