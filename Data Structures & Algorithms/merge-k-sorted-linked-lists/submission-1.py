# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergetwolist(self,l1,l2):
        prev1=l1
        prev2=l2
        dummy=ListNode(0)
        prev=dummy

        while prev1 and prev2:
            if prev1.val<=prev2.val:
                prev.next=prev1
                prev1=prev1.next
            else:
                prev.next=prev2
                prev2=prev2.next
            prev=prev.next
        while prev1:
            prev.next=prev1
            prev1=prev1.next
            prev=prev.next
        while prev2:
            prev.next=prev2
            prev2=prev2.next
            prev=prev.next
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result=ListNode(0)
        result=result.next
        for list in lists:
            result=self.mergetwolist(list,result)
        return result
        