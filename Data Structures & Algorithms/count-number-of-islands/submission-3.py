DIR = [(0,1),(1,0),(0,-1),(-1,0)]
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        num = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.bfs(grid, row, col)
                    num+=1 

        return num

    def bfs(self, grid, row, col):
        queue = deque([(row, col)])
        visited = set([(row, col)])

        while queue:
            curr_row, curr_col = queue.popleft()
            grid[curr_row][curr_col] = '0'
            for delta_row, delta_col in DIR:
                next_row = curr_row + delta_row
                next_col = curr_col + delta_col
                if self.is_valid(grid, next_row, next_col, visited):
                    queue.append((next_row, next_col))
                    visited.add((next_row, next_col))
    
    def is_valid(self, grid, row, col, visited):
        if row < 0 or row >= len(grid):
            return False 
        if col < 0 or col >= len(grid[0]):
            return False
        if (row, col) in visited:
            return False
        return grid[row][col]=="1"
                



    

        