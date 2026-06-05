# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxi=0
    def maxtree(self,root):
        left=0
        right=0
        if root is None:
            return 0
        if root.left:
            left=1+self.maxtree(root.left)
        if root.right:
            right=1+self.maxtree(root.right)
        self.maxi=max(self.maxi,left+right)
        return max(left,right)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxtree(root)
        return self.maxi
        