# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balance=True
    def balancetree(self,root):
        left,right=0,0
        if root is None:
            return 0
        if root.left:
            left=1+self.balancetree(root.left)
        if root.right:
            right=1+self.balancetree(root.right)
        if left>right:
            if left-right>1:
                self.balance=False
        else:
            if right-left>1:
                self.balance=False
        return max(left,right)

        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        final=self.balancetree(root)
        return self.balance
        