# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final=[]
        if root is None:
            return []
        from collections import deque
        queue=deque([root])
        while len(queue)>0:
            len_q=len(queue)
            print(len_q)
            for i in range(len_q):
                current_node=queue.popleft()
                if i==len_q-1:
                    final.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return final
                    
        