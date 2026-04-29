from collections import deque
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    COLS = 0
    ROWS = 0
    def islandsAndTreasure(self, grid: List[List[int]]) -> list:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        dist = -1
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] == 0:
                    dist = 0
                elif grid[row][col] == 2147483647:
                    dist = self.bfs(grid, row, col)
                elif grid[row][col] == -1:
                    dist = -1
                grid[row][col] = dist


    def bfs(self, grid, row, col):
        queue = deque([])
        visited = set()
        queue.append([row, col])
        visited.add((row, col))

        dis = 0
        while queue:
            for i in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                if grid[curr_row][curr_col] == 0:
                    return dis
                for delta_row, delta_col in DIR:
                    next_row = delta_row + curr_row
                    next_col = delta_col + curr_col

                    if self.is_valid(grid, next_row, next_col, visited):
                        visited.add((next_row, next_col))
                        queue.append([next_row, next_col])
            dis += 1
    
        return dis

    def is_valid(self, grid, row, col, visited):
        if row < 0 or row >= self.ROWS:
            return False 
        if col < 0 or col >= self.COLS:
            return False 
        if (row, col) in visited:
            return False 
        return grid[row][col] != -1





        