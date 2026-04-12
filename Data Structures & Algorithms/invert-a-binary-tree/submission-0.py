# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __invertree(self,current_node):
        if current_node is None:
            return None
        current_node.left=self.__invertree(current_node.left)
        current_node.right=self.__invertree(current_node.right)
        temp=current_node.left
        current_node.left=current_node.right
        current_node.right=temp
        return current_node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.__invertree(root)
        