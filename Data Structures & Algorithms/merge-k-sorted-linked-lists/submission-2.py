# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        
        def mergetwolists(list1,list2):
            dummy=ListNode(0)
            head1=list1
            head2=list2
            current=dummy
            while head1 is not None and head2 is not None:
                if head1.val<head2.val:
                    current.next=head1
                    head1=head1.next
                else:
                    current.next=head2
                    head2=head2.next
                current=current.next
            while head1 is not None:
                current.next=head1
                head1=head1.next
                current=current.next
            while head2 is not None:
                current.next=head2
                head2=head2.next
                current=current.next
            return dummy.next
        print(len(lists))
        if len(lists)==0:
            return None
        merge=lists[0]
        for i in range(1,len(lists)):
            merge=mergetwolists(merge,lists[i])
        return merge
        