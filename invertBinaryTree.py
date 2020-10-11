# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            new_tree = TreeNode(root.val if root else 0)
            
            new_tree.left = self.invertTree(root.right if root else None)
            new_tree.right = self.invertTree(root.left if root else None)
            
            return new_tree
        
        return None