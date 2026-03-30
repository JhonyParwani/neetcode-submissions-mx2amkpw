# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        prev=dummy
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                prev.next=list1
                list1=list1.next
            else:
                prev.next=list2
                list2=list2.next
            prev=prev.next
        while list1:
            prev.next=list1
            list1=list1.next
            prev=prev.next
        while list2:
            prev.next=list2
            list2=list2.next
            prev=prev.next
        return dummy.next
        
        
        

                
                
        