from collections import deque
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_isl = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    self.bfs(grid, row, col, visited)
                    num_isl += 1 
        return num_isl

    def bfs(self, grid, row, col, visited):
        queue = deque([(row, col)])
        while queue:
            curr_row, curr_col = queue.popleft()
            visited.add((curr_row, curr_col))
            for delta_row, delta_col in DIR:
                next_row = curr_row + delta_row
                next_col = curr_col + delta_col
                if self.is_valid(grid, next_row, next_col, visited):
                    queue.append((next_row, next_col))
    
    def is_valid(self, grid, row, col, visited):
        if row < 0 or row >= len(grid):
            return False 
        if col < 0 or col >= len(grid[0]):
            return False 
        if (row, col) in visited:
            return False
        return grid[row][col] == '1'

        