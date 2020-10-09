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
        tree = TreeNode()
        buf_tree = tree
        tree = self.doMerge(tree, t1, t2)
        return buf_tree
    
    @classmethod
    def doMerge(self, tree, t1, t2):
        tree.val = t1.val + t2.val
        
        if t1.left or t2.left:
            self.doLeft(tree, t1, t2)
        if t1.right or t2.right:
            self.doRight(tree, t1, t2)

        return tree

    @classmethod
    def doRight(self, tree, t1, t2):
        if t1.right and t2.right:
            tree.right = TreeNode()
            tree = tree.right
           
            return self.doMerge(tree, t1.right, t2.right)

        if t1.right and t2.right == None:
            tree.right = TreeNode()
            tree = tree.right
           
            return self.doMerge(tree, t1.right, TreeNode())
        
        if t1.right == None and t2.right:
            tree.right = TreeNode()
            tree = tree.right
         
            return self.doMerge(tree, TreeNode(), t2.right)
        
    @classmethod
    def doLeft(self, tree, t1, t2):
        if t1.left and t2.left:
            tree.left = TreeNode()
            tree = tree.left
         
            return self.doMerge(tree, t1.left, t2.left)
        
        if t1.left and t2.left == None:
            tree.left = TreeNode()
            tree = tree.left
         
            return self.doMerge(tree, t1.left, TreeNode())
        
        if t1.left == None and t2.left:
            tree.left = TreeNode()
            tree = tree.left
        
            return self.doMerge(tree, TreeNode(), t2.left)