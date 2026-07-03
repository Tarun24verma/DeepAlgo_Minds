"""
LeetCode: Next Greater Element I
Problem: Given two arrays nums1 and nums2 where nums1 is a subset of nums2,
for each element in nums1, find the next greater element in nums2.
The next greater element is the first element to the right that is greater.
Return -1 if no such element exists.

Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Time Complexity: O(n + m) where n = len(nums2), m = len(nums1)
Space Complexity: O(n) for the monotonic stack and hash map
"""

from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Use monotonic stack to efficiently find next greater elements.

    Approach:
    - Iterate through nums2 from right to left
    - Maintain a decreasing stack of values
    - For each element, pop all smaller values (they found their next greater)
    - The remaining top of stack is the next greater element (if exists)
    - Store results in a hash map for O(1) lookup
    - For each element in nums1, look up the answer from the hash map
    """
    # Build next greater map for all elements in nums2
    next_greater_map = {}
    stack = []  # maintains indices in decreasing order of values

    # Iterate nums2 from right to left
    for num in reversed(nums2):
        # Pop all elements smaller than current number
        while stack and stack[-1] < num:
            stack.pop()

        # If stack has elements, top is the next greater element
        if stack:
            next_greater_map[num] = stack[-1]
        else:
            next_greater_map[num] = -1

        # Push current number
        stack.append(num)

    # Look up answers for nums1
    return [next_greater_map[num] for num in nums1]


# Test cases
if __name__ == "__main__":
    # Test 1: Basic case
    nums1_1 = [4, 1, 2]
    nums2_1 = [1, 3, 4, 2]
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Output: {nextGreaterElement(nums1_1, nums2_1)}")
    print(f"Expected: [-1, 3, -1]\n")

    # Test 2: All elements have next greater
    nums1_2 = [2, 4]
    nums2_2 = [1, 2, 3, 4]
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Output: {nextGreaterElement(nums1_2, nums2_2)}")
    print(f"Expected: [3, -1]\n")

    # Test 3: No next greater elements
    nums1_3 = [1, 2, 3]
    nums2_3 = [3, 2, 1]
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Output: {nextGreaterElement(nums1_3, nums2_3)}")
    print(f"Expected: [-1, -1, -1]\n")

    # Test 4: Single element
    nums1_4 = [1]
    nums2_4 = [1, 2]
    print(f"Input: nums1 = {nums1_4}, nums2 = {nums2_4}")
    print(f"Output: {nextGreaterElement(nums1_4, nums2_4)}")
    print(f"Expected: [2]\n")

    # Test 5: Larger array with mixed results
    nums1_5 = [2, 4, 1]
    nums2_5 = [1, 2, 3, 4, 5]
    print(f"Input: nums1 = {nums1_5}, nums2 = {nums2_5}")
    print(f"Output: {nextGreaterElement(nums1_5, nums2_5)}")
    print(f"Expected: [3, 5, 2]")
