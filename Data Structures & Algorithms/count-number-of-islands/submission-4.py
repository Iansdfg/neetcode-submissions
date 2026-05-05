from collections import deque
DIR = [(0,1), (1,0), (0,-1), (-1,0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.bfs(grid, visited, row, col)
                    res += 1 
        
        return res 

    def bfs(self, grid, visited, row, col):
        queue = deque([(row, col)])
        visited.add((row, col))

        while queue:
            print(queue)
            curr_row, curr_col = queue.popleft()
            grid[curr_row][curr_col] = '0'
            for delta_row, delta_col in DIR:
                next_row = curr_row + delta_row
                next_col = curr_col + delta_col
                if self.is_valid(grid, visited, next_row, next_col):
                    queue.append((next_row, next_col))
                    visited.add((next_row, next_col))

    def is_valid(self, grid, visited, row, col):
        if row < 0 or row >= len(grid):
            return False 
        if col < 0 or col >= len(grid[0]):
            return False 
        if tuple([row, col])in visited:
            return False
        return grid[row][col] == '1'
        