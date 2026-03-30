# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        temp=slow.next
        prev=head
        while prev.next!=temp:
            prev=prev.next
        while temp and temp.next:
            to_pick=temp.next
            temp.next=to_pick.next
            to_pick.next=prev.next
            prev.next=to_pick
        second=prev.next
        slow.next=None
        first=head
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
