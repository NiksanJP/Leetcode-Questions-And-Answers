"""

Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island = 0
        def helper(x,y):
            if grid[x][y] == "1":
                grid[x][y] = "0"
            
                if x != 0:
                    helper(x-1, y)
                if y != 0:
                    helper(x, y-1)
                if x != len(grid)-1:
                    helper(x+1,y)
                if y != len(grid[0])-1:
                    helper(x, y+1)
                
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island += 1
                    helper(i, j)
        
        return island