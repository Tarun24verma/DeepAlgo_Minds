class Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=Tree(20)
root.left=Tree(8)
root.right=Tree(22)
root.left.left=Tree(5)
root.left.right=Tree(3)
root.left.right.left=Tree(10)
root.left.right.right=Tree(14)
root.right.right=Tree(25)
root.right.left=Tree(4)
root.right.right.left=Tree(28)
def Tprint(root):
    if not root:
        return
    Tprint(root.left)
    if root.left==None and root.right==None:
        print(root.data)
    Tprint(root.right)
Tprint(root)
# s=4
# found=0
# def Search(root,s):
#     if root:
#         if root.data==None:
#             print(False)
#         if root.data == s:
#             print(True)
#         elif s < root.data:
#             return Search(root.left,s)
#         else:
#             return Search(root.right,s)
# Search(root,s)
