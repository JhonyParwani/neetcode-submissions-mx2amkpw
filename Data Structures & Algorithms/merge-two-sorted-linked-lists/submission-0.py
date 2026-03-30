# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        head=dummy
        t1=list1
        t2=list2
        while t1 is not None and t2 is not None:
            if t1.val>t2.val:
                head.next=t2
                t2=t2.next
            else:
                head.next=t1
                t1=t1.next
            head=head.next
        while t1 is not None:
            head.next=t1
            t1=t1.next
            head=head.next

        while t2 is not None:
            head.next=t2
            t2=t2.next
            head=head.next

        return dummy.next
        
        
        
        
        
        