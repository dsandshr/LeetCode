# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1
        return 0