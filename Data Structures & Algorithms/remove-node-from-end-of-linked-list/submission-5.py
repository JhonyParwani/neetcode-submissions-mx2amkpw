# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        temp=head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        to_loop=count-n
        temp=head
        for _ in range(to_loop):
            temp=temp.next
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        l=to_loop
        for _ in range(l):
            prev=prev.next
        print(prev.val,temp.val)
        prev.next=temp.next
        temp.next=None
        head=dummy.next
        return head

        