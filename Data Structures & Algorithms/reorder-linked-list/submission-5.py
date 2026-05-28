# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast.next is not None and fast.next.next is not None:
            fast=fast.next.next
            slow=slow.next
        current=slow.next
        slow.next=None
        prev=None
        while current is not None:
            after=current.next
            current.next=prev
            prev=current
            current=after
        dummy=ListNode(0)
        current=dummy
        count=0
        while head is not None and prev is not None:
            if count%2==0:
                current.next=head
                head=head.next
            else:
                current.next=prev
                prev=prev.next
            count+=1
            current=current.next
        while head is not None:
            current.next=head
            head=head.next
            current=current.next
        while prev is not None:
            current.next=prev
            prev=prev.next
            current=current.next




        

        