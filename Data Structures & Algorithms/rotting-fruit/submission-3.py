DIRCTIONS = [(0, 1),(1, 0),(-1, 0),(0, -1)]
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1 
                
        time, fresh_remain = self.bfs(grid, queue, fresh)
        if fresh_remain > 0:
            return -1 
        return time

    def bfs(self, grid, queue, fresh):
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                for delta_row, delta_col in DIRCTIONS:
                    next_row = curr_row + delta_row
                    next_col = curr_col + delta_col
                    if self.is_valid(grid, next_row, next_col):
                        queue.append((next_row, next_col))
                        grid[next_row][next_col] = 2
                        fresh -= 1 
            time += 1 
        return time, fresh
    
    def is_valid(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return False 
        if col < 0 or col >= len(grid[0]):
            return False 
        if grid[row][col] != 1:
            return False 
        return True

