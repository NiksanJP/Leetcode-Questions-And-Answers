"""
Trafic Map
Hard

Consider a map of city streets, in form of a grid

you would like to know if it is possible to make your way to the exit, under the following rules
- you begin from the left side of the square in the top-keft corner
- the exit is on the right side of the square in the bottom-right corner
- you must travel along a connected path between squares

You are given directions, a matrix of integers representing the grid of streets, 
where each integer corresponds to a different type of road

- 0 stands for 
 =======
 |     |
 | --- |
 |     |
 =======
 
 - 1 stands for 
 =======
 |     |
 |  |  |
 |     |
 =======
 
 - 2 stands for 
 =======
 |     |
 | --  |
 |  |  |
 =======
 
 - 3 stands for 
 =======
 |     |
 |  -- |
 |  |  |
 =======
 
  - 4 stands for 
 =======
 |  |  |
 |  -- |
 |     |
 =======
 
  - 5 stands for 
 =======
 |  |  |
 | --  |
 |     |
 =======
 
 You task is to return true if it's possible to reach the exit and flase otherwise

"""

Map_False = [
    
    [0, 2, 0, 1, 3, 2],
    [2, 1, 4, 5, 0, 0],
    [3, 1, 3, 0, 0, 2],
    [1, 0, 1, 0, 2, 1],
    [1, 4, 1, 2, 1, 1],
    [4, 0, 5, 3, 4, 4]
    
]

Map_True = [
    
    [0, 2, 0, 1, 3, 2],
    [2, 1, 4, 5, 0, 0],
    [3, 4, 0, 0, 0, 2],
    [1, 0, 1, 0, 2, 1],
    [1, 4, 1, 2, 1, 1],
    [4, 0, 5, 3, 4, 4]
    
]

def solution(Map):
    endX, endY = len(Map) - 1, len(Map[0]) - 1
    x, y = 0, 0
    canEnd = False
    
    
    def helper(x,y):
        if x == endX and y == endY and canEnd == False:
            canEnd = True
            return
        
        if Map[x][y] == 0:
            if y != endY:
                y += 1
                if Map[x][y] in [2, 5, 0]:
                    helper(x, y)
                else:
                    return
        
        elif Map[x][y] == 1:
            if x != endX:
                x += 1
                if Map[x][y] in [1, 4, 5]:
                    helper(x, y)
                else:
                    return
            
        elif Map[x][y] == 2 and x != endX and y != endY:
            x += 1
            y += 1
            if Map[x][y] in [1, 4, 5]:
                helper(x,y)
            else:
                return
        
        elif Map[x][y] == 3 and x != endX and y != endY:
            x -= 1
            y += 1
            if Map[x][y] in [0, 2, 5]:
                helper(x,y)
            else:
                return
            
        elif Map[x][y] == 4 and x != endX and y != endY:
            x += 1
            y += 1
            if Map[x][y] in [0, 2, 5]:
                helper(x,y)
            else:
                return    
            
        elif Map[x][y] == 5 and x != endX and y != endY:
            y += 1
            x -= 1
            if Map[x][y] in [1, 2, 3]:
                helper(x, y)
    
    helper(x, y)            
    return canEnd
        
print(solution(Map_True))