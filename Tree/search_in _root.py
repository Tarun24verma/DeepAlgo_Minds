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
ele=7
def TSearch(root,ele,side):
    if root:
        if root.data==ele:
            print(side)
        TSearch(root.left,ele,side="left")
        TSearch(root.right,ele,side="right")
        return root
TSearch(root,ele,side=None)