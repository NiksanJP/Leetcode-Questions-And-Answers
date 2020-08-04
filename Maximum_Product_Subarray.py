"""
    Maximum Product Subarray
    
    Medium
    
    Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

class Solution(object):
    def maxProduct(self, a):
        ans = max_prod = min_prod = a[0]                       
        for x in a[1:]:
            max_prod, min_prod = max(x, min_prod*x, max_prod*x), min(x, min_prod*x, max_prod*x) 
            ans = max(ans, max_prod)
        return ans