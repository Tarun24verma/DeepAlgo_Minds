from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        solution = []
        def Tprint(node):
            if node:
                solution.append(node.val)
                Tprint(node.left)
                Tprint(node.right)
        Tprint(root)
        return solution
        