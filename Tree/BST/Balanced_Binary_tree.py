from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    balance=True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):            
            if root is None:
                return -1
            left_height=height(root.left)
            right_height=height(root.right)
            self.balance=self.balance and left_height<=right_height+1 and left_height>=right_height-1
            return 1+max(left_height,right_height)
        height(root)
        return self.balance





# class BST():
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None
# root=BST(1)
# root.left=BST(2)
# root.right=BST(2)
# root.left.left=BST(3)
# root.left.right=BST(3)
# root.left.left.left=BST(4)
# root.left.left.right=BST(4)
# balance=True
# def height(root):
#     global balance
#     if root is None:
#         return -1
#     left_height=height(root.left)
#     right_height=height(root.right)
#     balance=balance and left_height<=right_height+1 and left_height>=right_height-1
#     return 1+max(left_height,right_height)
# a=height(root)
# print(a)
# print(balance)