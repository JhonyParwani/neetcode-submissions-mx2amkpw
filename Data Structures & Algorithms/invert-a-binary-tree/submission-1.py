# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __inverttree(self,node):
        if node is None:
            return 
        left=self.__inverttree(node.left)
        right=self.__inverttree(node.right)
        temp=left
        node.left=node.right
        node.right=temp
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node=self.__inverttree(root)
        return node
        