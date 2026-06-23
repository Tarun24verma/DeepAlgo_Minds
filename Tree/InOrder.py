from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        solution=[]
        def Tprint(node):
            if node:
                Tprint(node.left)
                solution.append(node.val)
                Tprint(node.right)
                return node
        Tprint(root)
        return solution