"""

Battleships in a Board
Medium

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X

In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

"""

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def helper(x, y, vertical):
            if board[x][y] == "X":
                board[x][y] = "."
                
                if vertical:
                    if x != 0 :
                        helper(x - 1, y, vertical)
                    if x != len(board) - 1:
                        helper(x + 1, y, vertical)
                else:
                    if y != 0:
                        helper(x, y - 1, vertical)
                    if y != len(board[0]) - 1:
                        helper(x, y + 1, vertical)
                
        ships = 0
        vFalse = hFalse = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if i != len(board) - 1:
                        if board[i + 1][j] == "X":
                            helper(i,j, True)
                            ships += 1
                        else:
                            vFalse = True
                    
                    if j != len(board[0]) - 1:
                        if board[i][j + 1] == "X":
                            helper(i,j, False)
                            ships += 1
                        else:
                            hFalse = True
                    
                    if board[i][j] == "X":
                        ships += 1
                        board[i][j] = "."
                    
                    vFalse = hFalse = False
                        
        return ships