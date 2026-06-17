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

def insert_node(val,pos,head):
    l=0
    perm_head=head
    new_node=Node(val)
    last_node=None
    while head != None:
        l+=1
        if head.next is None:
            last_node=head
        head=head.next
    head=perm_head
    if pos==1:
        new_node.next=head
        perm_head=new_node
    elif l<pos:
        last_node.next=new_node
    else:
        cur_pos=1
        while cur_pos<pos-1:
            cur_pos+=1
        temp=head.next
        head.next=new_node
        new_node.next=temp
    return perm_head

k=int(input())

def delete_node(pos, head):
    cur_pos=0
    perm_head=head
    temp_head=None
    if pos==1:
        perm_head=head.next
        head.next=None
    else:
        while cur_pos<pos-2:
            cur_pos+=1
            head=head.next
        temp_head=head.next
        temp_head=temp_head.next
        head.next=temp_head
    return perm_head
y=int(input())
head=insert_node(k,y,head)
while head!=None:
    print(head.data)
    head=head.next