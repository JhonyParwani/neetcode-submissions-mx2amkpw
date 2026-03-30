# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        prev=dummy
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            sum=v1+v2+carry
            digit=sum%10
            carry=sum//10
            prev.next=ListNode(digit)
            prev=prev.next
            if l1 and l2:
                l1=l1.next
                l2=l2.next
            elif l1:
                l1=l1.next
            elif l2:
                l2=l2.next
            print(carry)
        return dummy.next


        