class Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=Tree(20)
root.left=Tree(10)
root.right=Tree(25)
root.left.left=Tree(9)
root.left.left.left=Tree(8)
root.left.right=Tree(15)
root.right.left=Tree(22)
root.right.right=Tree(30)
def large(root):
    if root:
        if root.right:
            large(root.right)
        else:
           print(root.data)
large(root)
