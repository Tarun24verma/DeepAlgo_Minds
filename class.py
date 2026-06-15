class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
node_1=Node(1)
node_2=Node(2)
node_3=Node(3)
node_4=Node(4)
node_5=Node(5)
node_1.next=node_2
node_2.next=node_3
node_3.next=node_4
node_4.next=node_5
head=node_1
while head != None:
    print(head.data)
    head=head.next