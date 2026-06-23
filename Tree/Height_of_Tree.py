class Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=Tree(4)
root.left=Tree(5)
root.right=Tree(6)
root.left.left=Tree(3)
root.left.left.left=Tree(7)
root.left.right=Tree(2)
root.left.right.left=Tree(10)
root.left.right.right=Tree(11)
root.right.left=Tree(1)
def Height(root):
    if root is None:
        return -1
    if root:
        left_height = Height(root.left)
        right_height = Height(root.right)
        return 1 + max(left_height,right_height)
print(Height(root))