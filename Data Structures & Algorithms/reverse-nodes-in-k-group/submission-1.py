# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        end= prev
        count=0
        while end:
            for _ in range(k):
                if end is None:
                    break
                end=end.next
            if end:
                new_head=end.next
            temp=prev.next
            while end is not None and temp.next!=new_head:
                to_pick=temp.next
                temp.next=to_pick.next
                to_pick.next=prev.next
                prev.next=to_pick
            end=temp
            prev=temp
        return dummy.next

        