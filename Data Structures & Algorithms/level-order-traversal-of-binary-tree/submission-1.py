# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        final=[]
        queue_list=[]
        from collections import deque
        queue=deque([root])
        level=0
        while len(queue)>0:
            len_q=len(queue)
            final.append([])
            for _ in range(len_q):
                current_node=queue.popleft()
                final[level].append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            level+=1
        return final


        


            

        



        



        