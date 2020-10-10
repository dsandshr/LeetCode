# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 or t2:
            new_tree = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        
            new_tree.left = self.mergeTrees((t1.left if t1 else None), (t2.left if t2 else None))
            new_tree.right = self.mergeTrees((t1.right if t1 else None), (t2.right if t2 else None))
        
            return new_tree
        
        return None