from collections import deque
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_isl = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.bfs(grid, row, col)
                    num_isl += 1 
        return num_isl

    def bfs(self, grid, row, col):
        queue = deque([(row, col)])

        while queue:
            curr_row, curr_col = queue.popleft()
            grid[curr_row][curr_col] = '0'
            for delta_row, delta_col in DIR:
                next_row = curr_row + delta_row
                next_col = curr_col + delta_col
                if self.is_valid(grid, next_row, next_col):
                    queue.append((next_row, next_col))
    
    def is_valid(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return False 
        if col < 0 or col >= len(grid[0]):
            return False 
        return grid[row][col] == '1'

        