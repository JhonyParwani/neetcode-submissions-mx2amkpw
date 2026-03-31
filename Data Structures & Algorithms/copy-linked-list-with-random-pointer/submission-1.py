"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap={}
        temp=head
        if not head:
            return None
        while temp:
            hashmap[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        copy_head=hashmap[temp]
        while temp:
            copy_node=hashmap[temp]
            copy_node.next=hashmap.get(temp.next)
            copy_node.random=hashmap.get(temp.random)
            temp=temp.next

        return copy_head
        