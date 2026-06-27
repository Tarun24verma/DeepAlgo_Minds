class Tree:
    def __init__(self,data):
        self.data=data
        self.node1=None
        self.node2=None
        self.node3=None
root=Tree(1)
root.node1=Tree(2)
root.node2=Tree(3)
root.node3=Tree(4)
root.node1.node1=Tree(5)
root.node1.node2=Tree(6)
root.node1.node3=Tree(7)
root.node2.node1=Tree(8)
root.node2.node3=Tree(9)
root.node3.node3=Tree(10)
def iter(root):
    if root:
        print(root.data)
        iter(root.node1)
        iter(root.node2)
        iter(root.node3)
        return root
iter(root)