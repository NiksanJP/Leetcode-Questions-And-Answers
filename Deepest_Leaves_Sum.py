"""

Deepest Leaves Sum
Medium

Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.maxDepth = 0
        
        def helper(node, depth):
            if not node.left and not node.right:
                if depth > self.maxDepth:
                    self.maxDepth = depth
                    self.sum = 0
                if depth == self.maxDepth:
                    self.sum += node.val
            
            if node.left:
                helper(node.left,depth + 1)
            if node.right:
                helper(node.right,depth + 1)
        
        helper(root, 0)
        return self.sum