DIRCTIONS = [(0, 1),(1, 0),(-1, 0),(0, -1)]

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    print(row, col)
                    self.bfs(grid, row, col)
                    island += 1 
        return island

    def bfs(self, grid, row, col):
        visited = set()
        queue = deque([(row, col)])
        while queue:
            curr_row, curr_col = queue.popleft()
            visited.add((curr_row, curr_col))
            grid[curr_row][curr_col] = '0'
            for delta_row, delta_col in DIRCTIONS:
                next_row = curr_row + delta_row
                next_col = curr_col + delta_col
                if self.is_valid(grid, next_row, next_col, visited):
                    queue.append((next_row, next_col))

    def is_valid(self, grid, row, col, visited):
        if row < 0 or row >= len(grid):
            return False 
        if col < 0 or col >= len(grid[0]):
            return False 
        if grid[row][col] == '0':
            return False 
        return (row, col) not in visited

        
                    


        