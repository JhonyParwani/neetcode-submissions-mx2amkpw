# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __issametree(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        elif (node1 is None and node2 is not None) or (node2 is None and node1 is not None) :
            return False
        if node1.val!=node2.val:
            return False
        left=self.__issametree(node1.left,node2.left)
        right=self.__issametree(node1.right,node2.right)
        final=left and right
        return final

        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        finalp=self.__issametree(p,q) 
        return finalp       
        