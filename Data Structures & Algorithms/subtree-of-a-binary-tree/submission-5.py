# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checksubtree(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        if (node1 is None and node2 is not None) or (node2 is None and node1 is not None):
            return False
        if node1.val!=node2.val:
            return False
        left=self.checksubtree(node1.left,node2.left)
        right=self.checksubtree(node1.right,node2.right)
        final_result=left and right
        return final_result

        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False
        if root.val==subRoot.val:
            if self.checksubtree(root,subRoot):
                return True

        left=self.isSubtree(root.left,subRoot)
        right=self.isSubtree(root.right,subRoot)
            
        
        return left or right
        
                

        