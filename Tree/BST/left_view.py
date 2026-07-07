class BST():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=BST(1)
root.left=BST(2)
root.right=BST(3)
root.left.left=BST(4)
root.left.right=BST(5)
root.left.right.left=BST(6)
left=[]
level=0
def lvl(root,level,left):
    if not root: return 
    if level == len(left): left.append(root.data)
    lvl(root.left,level+1,left)
    lvl(root.right,level,left)       
    return
lvl(root,level,left)

print(left)