from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        ph=head
        while head:
            head=head.next
            length+=1
        head=ph
        mid=(length//2)+2
        head.next
        length=0
        while head:
            head=head.next
            length+=1
            if length==mid:
                break
        return head