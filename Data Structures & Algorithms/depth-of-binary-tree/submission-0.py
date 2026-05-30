# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __maxdepth(self,node):
        if node is None:
            return 0
        
        left=self.__maxdepth(node.left)
        right=self.__maxdepth(node.right)
        return 1 + max(left,right)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi=self.__maxdepth(root)
        return maxi
        