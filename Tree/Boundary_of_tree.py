class Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.left.right=Tree(5)
root.left.right.left=Tree(8)
root.left.right.right=Tree(9)
root.right.left=Tree(6)
root.right.right=Tree(7)
bound=[]
def left_b(root,bound):
    if root:
        if root.right or root.left:
            bound.append(root.data)
            left_b(root.left,bound)
            return
        return
    return
def leaf(root,bound):
    if root:
        if not root.right and not root.left:
            bound.append(root.data)
        leaf(root.left,bound)
        leaf(root.right,bound)
        return
    return
def right_b(root,bound):
    if root:return
left_b(root,bound)
leaf(root,bound)
print(bound)