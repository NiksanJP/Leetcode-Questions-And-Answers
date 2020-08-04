"""
Count Number of Teams
Medium

here are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5

"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def dfs(i: int, prefix: List[int], increasing: bool) -> int:
            if len(prefix) == 3: return 1
            if i == len(rating): return 0
            result = 0
            rate = rating[i]
            if (increasing and prefix[-1] < rate) or (not increasing and prefix[-1] > rate):
                result += dfs(i+1, prefix + [rate], increasing)
            result += dfs(i+1, prefix, increasing)
            return result

        result = 0
        for i in range(len(rating)):
            result += dfs(i + 1, [rating[i]], True) + dfs(i + 1, [rating[i]], False)
        return result
