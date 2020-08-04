"""


Sum of Nodes with Even-Valued Grandparent
Medium

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

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
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        
        def helper(root):
            if not root:
                return 
            if root.val %2 == 0:
                if root.left:
                    if root.left.left:
                        self.sum += root.left.left.val
                    if root.left.right:
                        self.sum += root.left.right.val
                if root.right:
                    if root.right.left:
                        self.sum += root.right.left.val
                    if root.right.right:
                        self.sum += root.right.right.val
            if root.left:
                helper(root.left)
            
            if root.right:
                helper(root.right)
            
        helper(root)
        return self.sum