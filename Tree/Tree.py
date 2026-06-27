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
def Tprint(root):
    if not root:
        return
    Tprint(root.right)
    print(root.data)
    Tprint(root.left)
Tprint(root)
s=21
found=0
def Search(root,s):
    if root:
        if root.data==None:
            print(False)
        if root.data == s:
            print(True)
        elif s < root.data:
            return Search(root.left,s)
        else:
            return Search(root.right,s)
Search(root,s)
